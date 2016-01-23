from urllib2 import urlopen
from xml.dom import minidom

ny = urlopen('https://events.stanford.edu/xml/eventlist.xml')

pets = minidom.parseString(ny.read())
ny.close()

title = pets.getElementsByTagName('title')
for name in names:
	print name.firstChild.nodeValue