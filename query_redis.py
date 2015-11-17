# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 02:12:17 2015

@author: Nayak
"""
import pip

def install(package):
    pip.main(['install', redis])

import redis

r_server = redis.from_url("redis://h:pfakc6aj500pgttocvmqcj541c@ec2-54-83-59-218.compute-1.amazonaws.com:9979")

x = raw_input("Please enter the Player ID to retrieve his details: ")


print "Player Name: ", r_server.hvals(x)[0]
print "Team Name: ", r_server.hvals(x)[1]
print "Player Rating: ", r_server.hvals(x)[2]

low = raw_input("Enter lower bound for FIFA rating")    
high = raw_input("Enter upper bound for FIFA rating")    

for x in range(1,100):
    if r_server.hvals(x)[2] > low and r_server.hvals(x)[2] < high:
        print "Player Name: " + r_server.hvals(x)[0] + " | Team Name: " + r_server.hvals(x)[1] + " | Player Rating: " + r_server.hvals(x)[2] 
        #print "Team Name: ", r_server.hvals(x)[1]
        #print "Player Rating: ", r_server.hvals(x)[2]
    
