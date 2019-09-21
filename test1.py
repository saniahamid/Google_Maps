# -*- coding: utf-8 -*-
"""
Spyder Editor

This file contains the code for my frist attempt to learn google maps api
this code returns a jason datastructure from orging to destination points
"""
import urllib.request
import json
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key =''
origin =input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
print(request)
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print(directions)