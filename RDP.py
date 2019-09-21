# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:38:48 2018

@author: sania

This code implements the RDP line genralization algorithm
"""

import urllib.request
import json
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
import pandas as pd

def distance(a, b):
    return  sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def point_line_distance(point, start, end):
    if (start == end):
        return distance(point, start)
    else:
        n = abs(
            (end[0] - start[0]) * (start[1] - point[1]) - (start[0] - point[0]) * (end[1] - start[1])
        )
        d = sqrt(
            (end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2
        )
        return n / d

def rdp(points, epsilon):
    """
    Reduces a series of points to a simplified version that loses detail, but
    maintains the general shape of the series.
    """
    dmax = 0.0
    index = 0
    for i in range(1, len(points) - 1):
        d = point_line_distance(points[i], points[0], points[-1])
#print(directions)

#for keys in directions['routes'][0]['legs'][0]:
#    print(keys)
    
        if d > dmax:
            index = i
            dmax = d
    if dmax >= epsilon:
        results = rdp(points[:index+1], epsilon)[:-1] + rdp(points[index:], epsilon)
    else:
        results = [points[0], points[-1]]
    return results

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key ='AIzaSyA4KgYzBZn9FBUTrmNjTqurimTJuAH7Qzc'

index = 5
df = pd.read_csv('200m_1.csv')
data = df.as_matrix()
print(data[index,0])
print(data[index,1])
print(data[index,2])
print(data[index,3])

origin = str(data[index,0])+"," + str(data[index,1])
destination = str(data[index,2])+"," + str(data[index,3])
#print(org)
#print(des)
#origin = '40.750252,-73.991478'#'40.749832,-73.991135'
#destination = '40.750774,-74.005547'#'40.783894,-73.977615'


nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
print(request)
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
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

points = list(zip(X_Coord, Y_Coord))
print(points)

list_points = rdp(points,0.0028)
print("The result returned is: " + str(list_points))

plt.plot(Y_Coord, X_Coord,marker='o')
n = range(len(directions['routes'][0]['legs'][0]['steps']))
for i, txt in enumerate(n):
    plt.annotate(str(int(txt)+1) ,xy = (Y_Coord[i],X_Coord[i]))
plt.figure()
plt.show()

a = []
b = []
c = zip(*list_points)
#print(list(c))
c = list(c)
print(len(c))
a = list(c[0])
b = list(c[1])


plt.plot(b,a,marker='X',color='orange')
#n = range(len(directions['routes'][0]['legs'][0]['steps']))
#for i, txt in enumerate(n):
#    plt.annotate(str(int(txt)+1) ,xy = (Y_Coord[i],X_Coord[i]))
#plt.figure()
plt.show()



