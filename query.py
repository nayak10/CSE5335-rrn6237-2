#import os
import psycopg2
#import urlparse
#import traceback

#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ["postgres://flxvzdgthifjqo:YCViVah6QaxrzLgfQoousIxrOC@ec2-54-204-7-145.compute-1.amazonaws.com:5432/d15ik4407jjv1q"])

try:
    conn = psycopg2.connect("dbname='d43brbvbt6ugl9' user='ywhsrpfxdaknkl' host='ec2-107-21-223-147.compute-1.amazonaws.com' password='dnYTje6Tvi_vDyGq9Z1Qsf5yhY'")
except psycopg2.Error as e:
    print "I am unable to connect to the database"

idinput = raw_input("Enter IMDB ID to query on: ")    
cur = conn.cursor()
query = "SELECT * from friends where imbdid like " + "'%" + idinput + "%'"
#cur.execute("""SELECT * from friends where imbdid = '%s' """ % (idinput))
cur.execute(query)
rows = cur.fetchall()

print "\nShow me the Episode:\n"
for row in rows:
    print "   ", row[0],"-----",row[1],"-----", row[2]


low = raw_input("Enter lower bound for IMDB rating")    
high = raw_input("Enter upper bound for IMDB rating")    
cur1 = conn.cursor()
query1 = "SELECT * from friends where imbdrating between "  + low + " and " + high + ";"

cur1.execute(query1)
rows1 = cur1.fetchall()

print "\nShows between the bound of IMDB ratings:\n"
for row1 in rows1:
    print "   ", row1[0],"-----",row1[1],"-----", row1[2]
