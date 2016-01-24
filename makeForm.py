#!/usr/bin/env python
# This code handles a request 
import string, time, math

t1 = time.time()

fD = open("database.csv")
Dlines = fD.readlines()
fD.close()
events = {}

for line_num in xrange(len(Dlines)):
  events[line_num] = Dlines[line_num].strip().split("\t")

default_tag_list = ['location', 'title', 'description_textonly', 'beginDate', 'categories', 'url'] #stanford

for s in events.values():
  print len(s)

matching = [s for s in events.values() if "Arts" in s[2]]

print matching


#matching = [i for i in enumerate(beginDate) if 'January 16, 2016' in i]     
#cat = search_for_elem(events, 'January 16, 2016')
#print matching
#print_elements(titles)
#print_elements(locationTexts)
#print_elements(descriptions)
#for title in titles:
#    print title.firstChild.nodeValue.encode('utf-8').strip()


  