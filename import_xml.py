from urllib2 import urlopen
from xml.dom import minidom
from pprint import pprint
from collections import defaultdict

def print_elements(eles):
    #prints out elements enclosed in tags
    for ele in eles:
        print ele.firstChild.nodeValue.encode('utf-8').strip()
        
events = defaultdict(list)
fout = open("output.dat", "w")
    
    
tag_list = ['title', 'locationText', 'description_textonly', 'url', 'locationText', 'beginDate', 'beginTime', 'endTime', 'tags', 'categories'] #this tag list works with the stanford xml
    
    

university = urlopen('https://events.stanford.edu/xml/eventlist.xml')
#Upen = urlopen('https://www.sas.upenn.edu/events/rss.xml')
#ny = urlopen('http://events.bc.edu/calendar.xml')
data = minidom.parseString(university.read())
university.close()


titles = data.getElementsByTagName(tag_list[0])
locationTexts = data.getElementsByTagName(tag_list[1])
descriptions = data.getElementsByTagName(tag_list[2])
print len(titles)
print len(locationTexts)
print len(descriptions)
for key_event in range(len(titles) - 1):
	events[key_event].append(titles[key_event + 1].firstChild.nodeValue.encode('utf-8').strip())
	events[key_event].append(locationTexts[key_event].firstChild.nodeValue.encode('utf-8').strip())
	events[key_event].append(descriptions[key_event].firstChild.nodeValue.encode('utf-8').strip())
	
for val in events.values():
    for element in val:
        fout.write("%s" %element)
    fout.write("\n")
    

#print_elements(titles)
#print_elements(locationTexts)
#print_elements(descriptions)
#for title in titles:
#    print title.firstChild.nodeValue.encode('utf-8').strip()
