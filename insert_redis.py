# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:54:33 2015

@author: Nayak
"""

import pip

def install(package):
    pip.main(['install', redis])

import csv
import redis

print "Inserting data into the database, may take upto 10 seconds\n"

r_server = redis.from_url("redis://h:pfakc6aj500pgttocvmqcj541c@ec2-54-83-59-218.compute-1.amazonaws.com:9979")

c=0
count = 0
with open('C:\\Users\\Nayak\\Desktop\\Book1.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        c = c+1  
        for col in row:
            if count == 3:
                count = 0
            if count == 0:
                r_server.hset(c, "PlayerName", col) 
            if count == 1:
                r_server.hset(c, "TeamName", col) 
            if count == 2:
                r_server.hset(c, "FifaRating", col) 
            count = count + 1