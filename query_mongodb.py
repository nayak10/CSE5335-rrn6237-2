print ("Please run the command --- pip install pymongo --- if pymongo is not installed on Heroku yet, and then run the command python query_mongodb.py")

from pymongo import MongoClient  

mongolab_uri = "mongodb://heroku_9crjjz3b:eo0hbm9sgq5lkre3503kr3prsr@ds055584.mongolab.com:55584/heroku_9crjjz3b"

client = MongoClient(mongolab_uri,
                     connectTimeoutMS=30000,
                     socketTimeoutMS=None,
                     socketKeepAlive=True)

db = client.get_default_database()

print ("Please make sure the data is already inserted using insert_mongodb.py\n")

prim = input("Enter the PlayerID to retrieve player")    
cursor = db.footballers.find({"PlayerID" : prim})
for document in cursor:
    print(str(document['PlayerID']) + "---" + document['PlayerName'] + "---" + document['TeamName'] + "---" + str(document['FifaRating']))

low = input("Enter lower bound for FIFA rating")    
high = input("Enter upper bound for FIFA rating")   
 
cursor1 = db.footballers.find({ "FifaRating" : { "$gte" :  low, "$lte" : high}})
for document in cursor1:
    print(str(document['PlayerID']) + "---" + document['PlayerName'] + "---" + document['TeamName'] + "---" + str(document['FifaRating']))

