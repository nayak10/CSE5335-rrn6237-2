# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 02:12:17 2015

@author: Nayak
"""

import os
import redis

#r_server = redis.from_url(os.environ.get("redis://h:pfakc6aj500pgttocvmqcj541c@ec2-54-83-59-218.compute-1.amazonaws.com:9979"))

#r_server = redis.Redis('redis://h:pfakc6aj500pgttocvmqcj541c@ec2-54-83-59-218.compute-1.amazonaws.com:9979') #this line creates a new Redis object and
                                    #connects to our redis server
r_server = redis.from_url("redis://h:pfakc6aj500pgttocvmqcj541c@ec2-54-83-59-218.compute-1.amazonaws.com:9979")

#r_server.set('test_key', 'test_value') #with the created redis object we can
                                        #submits redis commands as its methods
                                        
#print 'previous set key ' + r_server.get('test_key') # the previous set key is fetched

'''In the previous example you saw that we introduced a redis
data type: the string, now we will set an integer and try to
increase its value using redis object built-in methods'''

#r_server.set('counter', 1) #set an integer to a key
#r_server.incr('counter') #we increase the key value by 1, has to be int
#print 'the counter was increased! '+ r_server.get('counter') #notice that the key is increased now

#r_server.decr('counter') #we decrease the key value by 1, has to be int
#print 'the counter was decreased! '+ r_server.get('counter') #the key is back to normal


r_server.hset("1", "PlayerName", "Wayne Rooney")

r_server.hset("1", "TeamName", "MUFC")
r_server.hset("1", "FifaRating", "9.2")

x = raw_input("Please enter the Player ID to retrieve his details")

#print r_server.hkeys(x)

print "Player Name: ", r_server.hvals(x)[0]
print "Team Name: ", r_server.hvals(x)[1]
print "Player Rating: ", r_server.hvals(x)[2]
#print r_server.hgetall(x)
#r_server.hvals(x)[0]

'''Now we are ready to jump into another redis data type, the list, notice 
that they are exactly mapped to python lists once you get them'''
'''
r_server.rpush('list1', 'element1') #we use list1 as a list and push element1 as its element

r_server.rpush('list1', 'element2') #assign another element to our list
r_server.rpush('list2', 'element3') #the same

print 'our redis list len is: %s'% r_server.llen('list1') #with llen we get our redis list size right from redis

print 'at pos 1 of our list is: %s'% r_server.lindex('list1', 1) #with lindex we query redis to tell us which element is at pos 1 of our list
'''
'''sets perform identically to the built in Python set type. Simply, sets are lists but, can only have unique values.'''
'''
r_server.sadd("set1", "el1")
r_server.sadd("set1", "el2")
#r_server.sadd("set1", "el2")

print 'the members of our set are: %s'% r_server.smembers("set1")
'''