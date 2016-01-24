from urllib2 import urlopen
from xml.dom import minidom
from pprint import pprint
from collections import defaultdict

#def print_elements(eles):
    #prints out elements enclosed in tags
    #for ele in eles:
        #print ele.firstChild.nodeValue.encode('utf-8').strip()

def getElements(xmlData, tag_list_number):
	#default_tag_list = ['location', 'title', 'description', 'event:beginDateTime', 'categories', 'link'] #rutgers
	#default_tag_list = ['location', 'title', 'description', 'pubDate', 'categories', 'link']
	#default_tag_list = ['location', 'title', 'description', 'pubDate', 'categories', 'x-trumba:weblink'] #trumba
	default_tag_list = ['location', 'title', 'description_textonly', 'beginDate', 'categories', 'url'] #stanford
	#stanford = ['title', 'locationText', 'description_textonly', 'url', 'beginDate', 'beginTime', 'endTime', 'tags', 'categories'] #this tag list works with the stanford xml
	try:
		return xmlData.getElementsByTagName(default_tag_list[tag_list_number])
	except:
		return []
        
#def search_for_elem(diction, search_for):
#	matching = [i for i, x in enumerate(diction) if search_for in x]
#	print matching
#	return matching


events = defaultdict(list)
fout = open("output.dat", "w")
    

    

    
    

university = urlopen('https://events.stanford.edu/xml/eventlist.xml')
#university = urlopen('http://www.trumba.com/calendars/tufts.rss')
#university = urlopen('http://www.uni.edu/unicalendar/rss.xml')
#university = urlopen('https://ruevents.rutgers.edu/events/getEventsRss.xml')
#university = urlopen('https://www.sas.upenn.edu/events/rss.xml')
#university = urlopen('http://events.bc.edu/calendar.xml')
#university = urlopen('http://events.depaul.edu/calendar.xml')
#university = urlopen('http://services.rice.edu/events/dailyevents.cfm')
#university = urlopen('http://calendar.utexas.edu/calendar.xml')
#university = urlopen('http://events.colorado.edu/RSSSyndicator.aspx?category=&location=&type=N&binary=Y&keywords=&ics=Y')
#university = urlopen('http://www.purdue.edu/newsroom/rss/EventNews.xml')
data = minidom.parseString(university.read())
university.close()

#TODO: check that the data contains all the correct tags

titles = getElements(data, 1)
#locationTexts = getElements(data, 1)
#descriptions = getElements(data, 2)
descriptions = getElements(data, 2)

#url = getElements(data, 3)
beginDate = getElements(data, 3)
categories = getElements(data, 4)
url = getElements(data, 5)
#beginDate = getElements(data, 4)
#beginTime = getElements(bdata, 5)
#endTime = getElements(data, 6)
#event_tags = getElements(data, 7) #note: may be unigue to stanford
#categories = getElements(data, 8)
print len(titles)
#print len(locationTexts)
print len(descriptions)
print len(beginDate)
print len(categories)
print len(url)
flag_titles = 0
if len(titles) > len(descriptions):
	range_titles = len(titles) - 1
else:
	range_titles = len(titles)
	flag_titles = 1 
url_key_event_gap = 0

for key_event in range(range_titles):
        events[key_event].append("Purdue University") 
	if flag_titles:
		events[key_event].append(titles[key_event].firstChild.nodeValue.encode('utf-8').strip())
	else:
		events[key_event].append(titles[key_event + 1].firstChild.nodeValue.encode('utf-8').strip())
	#events[key_event].append(locationTexts[key_event].firstChild.nodeValue.encode('utf-8').strip())
	try:
	    events[key_event].append(descriptions[key_event].firstChild.nodeValue.encode('utf-8').strip())
        except:
            events[key_event].append('This descritiption is intentionally left blank')
	if key_event > 0:#comment for Stanford hack
	    events[key_event].append(beginDate[key_event - 1].firstChild.nodeValue.encode('utf-8').strip())#comment for Stanford hack
        else:#comment for Stanford hack
            events[key_event].append('Time')#comment for Stanford hack
	#events[key_event].append(beginDate[key_event].firstChild.nodeValue.encode('utf-8').strip()) #if there are no problems with date and event
	try:
	    events[key_event].append(categories[key_event].firstChild.nodeValue.encode('utf-8').strip())
        except:
            events[key_event].append('Uncategorized')
	try:#comment for Stanford hack
	    events[key_event].append(url[key_event].firstChild.nodeValue.encode('utf-8').strip())#comment for Stanford hack
        except:#comment for Stanford hack
            events[key_event].append('Link unavailable')#comment for Stanford hack
            

## Stanford hack:
#
#key_event_counter = 0
#            
#for url_counter in range(len(url)):
#        #print key_event
#        #print url_key_event_gap
#        if url[url_counter].firstChild.nodeValue.encode('utf-8').strip()[0] == 'h':
#            events[key_event_counter].append(url[url_counter].firstChild.nodeValue.encode('utf-8').strip())
#            key_event_counter += 1

	
for val in events.values():
    for element in val:
        fout.write("%s\t" %element)
    fout.write("\n")

matching = [s for s in events.values() if 'January 16, 2016' in s]
print matching
#matching = [i for i, x in enumerate(beginDate) if 'January 16, 2016' in x]     
#cat = search_for_elem(events, 'January 16, 2016')
#print cat
#print_elements(titles)
#print_elements(locationTexts)
#print_elements(descriptions)
#for title in titles:
#    print title.firstChild.nodeValue.encode('utf-8').strip()


