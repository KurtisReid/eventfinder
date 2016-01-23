from urllib2 import urlopen
from xml.dom import minidom
from pprint import pprint
from collections import defaultdict

#def print_elements(eles):
    #prints out elements enclosed in tags
    #for ele in eles:
        #print ele.firstChild.nodeValue.encode('utf-8').strip()

def getElements(xmlData, tag_list_number):
	default_tag_list = ['title', 'description', 'link', 'pubDate']
	#tag_list = ['title', 'locationText', 'description_textonly', 'url', 'beginDate', 'beginTime', 'endTime', 'tags', 'categories'] #this tag list works with the stanford xml
	return xmlData.getElementsByTagName(default_tag_list[tag_list_number])
        
events = defaultdict(list)
fout = open("output.dat", "w")
    

    

    
    

university = urlopen('https://events.stanford.edu/xml/eventlist.xml')
#Upen = urlopen('https://www.sas.upenn.edu/events/rss.xml')
#ny = urlopen('http://events.bc.edu/calendar.xml')
data = minidom.parseString(university.read())
university.close()

#TODO: check that the data contains all the correct tags

titles = getElements(data, 0)
#locationTexts = getElements(data, 1)
#descriptions = getElements(data, 2)
descriptions = getElements(data, 1)

#url = getElements(data, 3)
url = getElements(data, 2)
beginDate = getElements(data, 3)
#beginDate = getElements(data, 4)
#beginTime = getElements(data, 5)
#endTime = getElements(data, 6)
#event_tags = getElements(data, 7) #note: may be unigue to stanford
#categories = getElements(data, 8)
print len(titles)
#print len(locationTexts)
print len(descriptions)
flag_titles = 0
if len(titles) > len(descriptions):
	range_titles = len(titles) - 1
else:
	range_titles = len(titles)
	flag_titles = 1	

for key_event in range(range_titles):
	if flag_titles:
		events[key_event].append(titles[key_event].firstChild.nodeValue.encode('utf-8').strip())
	else:
		events[key_event].append(titles[key_event + 1].firstChild.nodeValue.encode('utf-8').strip())
	#events[key_event].append(locationTexts[key_event].firstChild.nodeValue.encode('utf-8').strip())
	events[key_event].append(descriptions[key_event].firstChild.nodeValue.encode('utf-8').strip())
	events[key_event].append(url[key_event].firstChild.nodeValue.encode('utf-8').strip())
	events[key_event].append(beginDate[key_event].firstChild.nodeValue.encode('utf-8').strip())

	
for val in events.values():
    for element in val:
        fout.write("%s" %element)
    fout.write("\n")
    

#print_elements(titles)
#print_elements(locationTexts)
#print_elements(descriptions)
#for title in titles:
#    print title.firstChild.nodeValue.encode('utf-8').strip()
