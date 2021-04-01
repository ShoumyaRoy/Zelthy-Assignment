"""
Assignment 3:
Write a python class that is able to return the flight distance between two cities given their
latitude and longitude coordinates.
Expected output:
$ python -m city_distance.py
> City 1: 51.5074 N, 0.1278 W
> City 2: 48.8566 N, 2.3522 E
> Output: City 1 and City 2 are 342.87 km apart
"""
from math import radians, cos, sin, asin, sqrt

def city_distance(latitude_one, latitude_two, longitute_one, longitude_two):
	longitute_one = radians(longitute_one)
	longitude_two = radians(longitude_two)
	latitude_one = radians(latitude_one)
	latitude_two = radians(latitude_two)
	
	# Haversine formula
	dlongitude = longitude_two - longitute_one
	dlatitude = latitude_two - latitude_one
	a = sin(dlatitude / 2)**2 + cos(latitude_one) * cos(latitude_two) * sin(dlongitude / 2)**2
	c = 2 * asin(sqrt(a))
	r = 6371 #radius of earth
	return(round(c * r, 2))
	
city_one = input("City 1: "); # 51.5074 N, 0.1278 W
city_one = city_one.replace(",","")
city_one = city_one.split()

city_two = input("City 2: "); # 48.8566 N, 2.3522 E
city_two = city_two.replace(",","")
city_two = city_two.split()

if city_one[1]=='S':
	latitude_one = -float(city_one[0])#51.5074
else:
	latitude_one = float(city_one[0])#51.5074

if city_one[3]=='W':
	longitute_one = -float(city_one[2])#-0.1278
else:
	longitute_one = float(city_one[2])#-0.1278

if city_two[1]=='S':
	latitude_two = -float(city_two[0])#48.8566
else:
	latitude_two = float(city_two[0])#48.8566

if city_two[3]=='W':
	longitude_two = -float(city_two[2])#2.3522
else:
	longitude_two = float(city_two[2])#2.3522

distance = city_distance(latitude_one, latitude_two, longitute_one, longitude_two)
print("Output: City 1 and City 2 are",distance,"km apart")
