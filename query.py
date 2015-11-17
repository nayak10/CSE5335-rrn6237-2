#import os
import psycopg2
#import urlparse

try:
    conn = psycopg2.connect("dbname='d15ik4407jjv1q' user='flxvzdgthifjqo' host='ec2-54-204-7-145.compute-1.amazonaws.com' password='YCViVah6QaxrzLgfQoousIxrOC'")
except:
    print "I am unable to connect to the database"

cur = conn.cursor()
cur.execute("""SELECT datname from pg_database""")
rows = cur.fetchall()

print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]