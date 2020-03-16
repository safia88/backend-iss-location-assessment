#!/usr/bin/env python

__author__ = 'Safia Ali'


import datetime
import json
import threading
import time
import turtle
import sys
import requests


def getAstronus():
    url = 'http://api.open-notify.org/astros.json'
    # response = requests.get(url)
    # result = json.loads(response.read())
    result = requests.get(url).json()

    print('Total Astronauts In Space: ', result['number'])

    people = result['people']

    for p in people:
        print(p['name'], ' in ', p['craft'])


def currentGeographicCoordinates():
    url = 'http://api.open-notify.org/iss-now.json'
    # response = request.urlopen(url)
    # result = json.loads(response.read())
    result = requests.get(url).json()

    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    print('Latitude: ', lat)
    print('Longitude: ', lon)

    return {'latitude': lat, 'longitude': lon}


def createCurrentCoordinatesgraphich(lat, lon):
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')

    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')

    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)

    iss.penup()
    iss.goto(lon, lat)

    # Indianapolis
    lat = 40.273502
    lon = -86.126976

    location = turtle.Turtle()
    location.penup()
    location.color('yellow')
    location.goto(lon, lat)
    location.dot(5)
    location.hideturtle()

    url = 'http://api.open-notify.org/iss-pass.json?lat=' + \
        str(lat) + '&lon=' + str(lon)
    # response = request.urlopen(url)
    # result = json.loads(response.read())
    result = requests.get(url).json()

    # print result
    over = result['response'][1]['risetime']
    location.write(time.ctime(over))


def main():
    print('========Part A=========')
    getAstronus()

    print('========Part B=========')
    coordinate = currentGeographicCoordinates()

    print('========Part C & D=========')
    createCurrentCoordinatesgraphich(
        coordinate['latitude'], coordinate['longitude'])


if __name__ == '__main__':
    main()
    # input("Press Enter to continue...")
    time.sleep(5)

# pip3 install requests
