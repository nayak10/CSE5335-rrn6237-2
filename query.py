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
    