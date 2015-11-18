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

db.footballers
result = db.footballers.delete_many({})
#print(result.deleted_count)

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

print("Data has been inserted\n")
print("---------------------Inserted data---------------------\n")
cursor = db.footballers.find()
for document in cursor:
    print(str(document['PlayerID']) + "---" + document['PlayerName'] + "---" + document['TeamName'] + "---" + str(document['FifaRating']))

