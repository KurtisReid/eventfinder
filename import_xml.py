from urllib2 import urlopen
from xml.dom import minidom
from pprint import pprint

def print_elements(eles):
    #prints out elements enclosed in tags
    for ele in eles:
        print ele.firstChild.nodeValue.encode('utf-8').strip()
        

    
    
tag_list = ['title', 'locationText', 'description_textonly', 'url', 'locationText', 'beginDate', 'beginTime', 'endTime', 'tags', 'categories'] #this tag list works with the stanford xml
    
    

university = urlopen('https://events.stanford.edu/xml/eventlist.xml')
#Upen = urlopen('https://www.sas.upenn.edu/events/rss.xml')
#ny = urlopen('http://events.bc.edu/calendar.xml')
data = minidom.parseString(university.read())
university.close()

titles = data.getElementsByTagName(tag_list[0])
locationTexts = data.getElementsByTagName(tag_list[1])
descriptions = data.getElementsByTagName(tag_list[2])
print_elements(titles)
print_elements(locationTexts)
print_elements(descriptions)
#for title in titles:
#    print title.firstChild.nodeValue.encode('utf-8').strip()
#print name.firstChild.nodeValue
