from urllib2 import urlopen
from xml.dom import minidom
from pprint import pprint

ny = urlopen('https://events.stanford.edu/xml/eventlist.xml')

pets = minidom.parseString(ny.read())
ny.close()

titles = pets.getElementsByTagName('title')
for title in titles:
    print title.firstChild.nodeValue.encode('utf-8').strip()