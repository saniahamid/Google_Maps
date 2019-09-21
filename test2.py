# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:42:45 2018

@author: nexts
"""

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyA4KgYzBZn9FBUTrmNjTqurimTJuAH7Qzc')

# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

print(geocode_result)