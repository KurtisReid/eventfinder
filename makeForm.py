#!/usr/bin/env python
# This code handles a request
import string, time, math


t1 = time.time()

fD = open("database.csv")
Dlines = fD.readlines()
fD.close()

events = {}

for line_num in xrange(len(Dlines)):
  q = filter(lambda x: x in string.printable, Dlines[line_num])
  events[line_num] = Dlines[line_num].strip().strip('%').decode('utf-8').split("\t")

default_tag_list = ['location', 'title', 'description_textonly', 'beginDate', 'categories', 'url'] #stanford

#requested_date = "27 Jan 2016"
#requested_city = "Boston"
#requested_cat = "Arts"

def find_event(requested_date, requested_cat, requested_city):
  Monthsabv = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  day, mon, year = requested_date.split(" ")
  date1 = day + " " + mon
  date2 = mon + " " + day
  matching = [i for i,s in enumerate(Monthsabv) if mon in s]
  date3 = Months[matching[0]] + " " + day
  date4 = str(matching[0]+1).zfill(2) + "-" + day
  Loc_Dict = {}
  Loc_Dict["Palo Alto"] = "Stanford University"
  Loc_Dict["Philadelphia"] = "Upenn"
  Loc_Dict["Boston"] = "Boston College"
  Loc_Dict["Boulder"] = "University of Colorado Boulder"
  Loc_Dict["New Brunswick"] = "Rutgers University"
  Loc_Dict["Austin"] = "UT"
  Loc_Dict["Chicago"] = "DePaul Univeristy"
  Loc_Dict["Houston"] = "Rice Univeristy"
  returnlist = []
  for s in range(len(events.values())):
    if date1 in events[s][3] or date2 in events[s][3] or date3 in events[s][3] or date4 in events[s][3]:
      if requested_cat in events[s][2]:
        if Loc_Dict[requested_city] in events[s][0]:
          returnlist.append("{}\t{}\t{}\t{}".format(events[s][2],events[s][1],events[s][3],events[s][0]).strip('%').split("\t"))
  return returnlist

#x = find_event(requested_date, requested_cat, requested_city)
#print x
#  if "Arts" in events[s][2] and "Jan 27" in events[s][3]:
#    print events[s][0]
#    print s
#    last = s
#matching_cat = [i for i,s in enumerate(events.values()) if "Arts" in s[2]]
#matching_date = [i for i,s in enumerate(events.values()[matching_cat]) if "27 Jan" in s[3]]

#print events[last]



#matching = [i for i in enumerate(beginDate) if 'January 16, 2016' in i]
#cat = search_for_elem(events, 'January 16, 2016')
#print matching
#print_elements(titles)
#print_elements(locationTexts)
#print_elements(descriptions)
#for title in titles:
#    print title.firstChild.nodeValue.encode('utf-8').strip()
