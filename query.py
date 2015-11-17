import os
import psycopg2
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["postgres://flxvzdgthifjqo:YCViVah6QaxrzLgfQoousIxrOC@ec2-54-204-7-145.compute-1.amazonaws.com:5432/d15ik4407jjv1q"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


cur = conn.cursor()
cur.execute("""SELECT datname from pg_database""")
rows = cur.fetchall()

print "\nShow me the databases:\n"
for row in rows:
    print "   ", row[0]