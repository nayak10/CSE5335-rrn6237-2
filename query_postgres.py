#import os
import psycopg2

try:
    conn = psycopg2.connect("dbname='dk3505cd5g85t' user='tajitmcdjbfhsb' host='ec2-107-21-223-72.compute-1.amazonaws.com' password='QIT6b8hSuViOe-iLGdoUdZ-MY-'")
except psycopg2.Error as e:
    print "I am unable to connect to the database"

idinput = raw_input("Enter Player ID to query on: ")    
cur = conn.cursor()
query = "SELECT * from footballers where playerid = "  + idinput + ";"
#cur.execute("""SELECT * from friends where imbdid = '%s' """ % (idinput))
cur.execute(query)
rows = cur.fetchall()

print "\nPlayer Details:\n"
for row in rows:
    print "   ", row[0],"-----",row[1],"-----", row[2],"-----", row[3]


low = raw_input("Enter lower bound for FIFA rating")    
high = raw_input("Enter upper bound for FIFA rating")    

cur1 = conn.cursor()
query1 = "SELECT * from footballers where fifarating between "  + low + " and " + high + "limit 20;"
#query1 = "SELECT * from footballers;"
cur1.execute(query1)
rows1 = cur1.fetchall()

print "\nShows players between the bound of FIFA ratings:\n"
for row1 in rows1:
    print "   ", row1[0],"-----",row1[1],"-----", row1[2],"-----", row1[3]
