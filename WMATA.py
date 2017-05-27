# -*- coding: utf-8 -*-
"""
Created on Sat May 27 14:58:33 2017

WMATA API Project

@author: Doug
"""
import json #Deals with json data format
try:
    from urllib.request import urlopen, Request # Works in Python 3
except ImportError:
    from urllib2 import urlopen, Request #Works in Python 2


    
demo_key = "e1eee2b5677f408da40af8480a5fd5a8" #WMATA Demonstration API key
incidents_url = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
hdrs = {'api_key': demo_key}
req = Request(incidents_url, headers=hdrs) #Provides API key
result = urlopen(req)
raw_data = result.read().decode('utf8')#decodes data using utf 8
data = json.loads(raw_data) #interprets raw data using json
print(data)
incidents = data["ElevatorIncidents"] #incidents is a list containing dictionaries

for i in incidents:
    if i["UnitType"]== "ELEVATOR":
        print(i["StationName"],i["LocationDescription"],i["TimeOutOfService"])



###Hex to decimal conversion

#first_line_placeholder = "The numeric value of: {}\n"
#first_line = first_line_placeholder.format(demo_key)
#integer_value_of_demo_key = int(demo_key, 16)
#second_line_placeholder = "in decimal is: {}\n"
#second_line = second_line_placeholder.format(integer_value_of_demo_key)
#print(first_line, second_line)

