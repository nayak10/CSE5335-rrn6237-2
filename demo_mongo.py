# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:10:23 2015

@author: Nayak
"""

from pymongo import MongoClient  
import csv

mongolab_uri = "mongodb://heroku_9crjjz3b:eo0hbm9sgq5lkre3503kr3prsr@ds055584.mongolab.com:55584/heroku_9crjjz3b"

client = MongoClient(mongolab_uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)

db = client.get_default_database()
#print db.collection_names()


#db.footballers
#result = db.footballers.delete_many({})
#print(result.deleted_count)

'''

with open('Book1.csv', 'rb') as f:
    reader = csv.reader(f)
    reader=list(reader)
k=1            

for row in reader:
    
    result = db.footballers.insert_one(
    {
        "PlayerID": k,
        "PlayerName" : str(row[0]),
        "TeamName" : str(row[1]),
        "FifaRating" : float(row[2])
    })
    k=k+1
'''
#print (result.inserted_id)
'''
cursor = db.footballers.find()
for document in cursor:
    print(str(document['PlayerID']) + "---" + document['PlayerName'] + "---" + document['TeamName'] + "---" + str(document['FifaRating']))
'''

low = input("Enter lower bound for FIFA rating")    
high = input("Enter upper bound for FIFA rating")   
 
cursor1 = db.footballers.find({ "FifaRating" : { "$gt" :  low, "$lt" : high}})
#cursor1 = db.footballers.find({ "FifaRating" : { "$gt": low } } )
for document in cursor1:
    print(str(document['PlayerID']) + "---" + document['PlayerName'] + "---" + document['TeamName'] + "---" + str(document['FifaRating']))

