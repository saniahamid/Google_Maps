# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:02:19 2018

@author: sania

This code takes in te origin and destination coordinates of a trip, makes connection with google maps API, returns
the coordinates of the steps involved the origin from the destination and visualizes it on a graph
"""
import urllib.request
import json
import matplotlib.pyplot as plt

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key =''
origin = '40.750252,-73.991478'#'40.749832,-73.991135'
destination = '40.750774,-74.005547'#'40.783894,-73.977615'


nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
print(request)
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
#print(directions)

#for keys in directions['routes'][0]['legs'][0]:
#    print(keys)
    
print(directions['routes'][0]['legs'][0]['start_address'])
print(directions['routes'][0]['legs'][0]['end_address'])

#print("STEPS ARE")
#for keys in directions['routes'][0]['legs'][0]['steps'][0]:
#    print(keys)
    
print('length of steps is: '+ str(len(directions['routes'][0]['legs'][0]['steps'])))

for  i in range(len(directions['routes'][0]['legs'][0]['steps'])):
    #print(directions['routes'][0]['legs'][0]['steps'][i]['html_instructions'])
    #print(directions['routes'][0]['legs'][0]['steps'][i]['start_location'])
    print("The start location is: "+str(directions['routes'][0]['legs'][0]['steps'][i]['start_location']))
    print("The end location is: "+str(directions['routes'][0]['legs'][0]['steps'][i]['end_location']))
    
X_Coord = []
Y_Coord = []
#DX_Coord = []
#DY_Coord = []

for i in range(len(directions['routes'][0]['legs'][0]['steps'])):
    X_Coord.append(directions['routes'][0]['legs'][0]['steps'][i]['start_location']['lat'])
    Y_Coord.append(directions['routes'][0]['legs'][0]['steps'][i]['start_location']['lng'])  
    
print('X_Coord matrix is: '+ str(X_Coord))
print('X_Coord matrix is: '+ str(Y_Coord))

plt.plot(Y_Coord, X_Coord,marker='o')
n = range(len(directions['routes'][0]['legs'][0]['steps']))
for i, txt in enumerate(n):
    plt.annotate(str(int(txt)+1) ,xy = (Y_Coord[i],X_Coord[i]))
plt.show()


