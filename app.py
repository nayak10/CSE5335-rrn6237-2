# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 22:38:05 2015

@author: Nayak
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 14:13:33 2015
@author: Nayak
"""
import urllib2
import json
#import psycopg2

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template

app = Flask(__name__)
db = SQLAlchemy(app)


class television1(db.Model):
    imdbid = db.Column(db.String(80), primary_key=True)
    title = db.Column(db.String(80), unique=False)
    imdbrating = db.Column(db.Float, unique=False)

    def __init__(self,imdbid,title,imdbrating):
        self.imdbid = imdbid
        self.title = title
        self.imdbrating = imdbrating

    #def __repr__(self):
     #   return '<television %r>' % self.username


@app.route("/")
def hello():
    return "Hello! Displaying Json Data"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://flxvzdgthifjqo:YCViVah6QaxrzLgfQoousIxrOC@ec2-54-204-7-145.compute-1.amazonaws.com:5432/d15ik4407jjv1q'
#db.reflect()

db.create_all()
db.session.commit()
        
@app.route("/lotsofdata")
def people():
       
    url = 'http://omdbapi.com/?t=sherlock&Season=1'
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string)    
    f.close()
    #print(parsed_json)
    #hello = parsed_json["Episodes"][0]["Title"]
    s = []
    for i in range(0,2):
         hello = []
         #hello.append(parsed_json["Episodes"][i]["Episode"])
         hello.append(parsed_json["Episodes"][i]["imdbID"])
         hello.append(parsed_json["Episodes"][i]["Title"])
         hello.append(parsed_json["Episodes"][i]["imdbRating"])
         s.append(hello)
         tv = television1(parsed_json["Episodes"][i]["imdbID"], parsed_json["Episodes"][i]["Title"], parsed_json["Episodes"][i]["imdbRating"])
         db.session.add(tv)
         db.session.commit()

    #conn = psycopg2.connect("dbname=test user=postgres")
    #cur = conn.cursor()
    #cur.execute("DROP TABLE test;")
    #cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
    
    return render_template('profile.html', s=s)


#admin = User1('admin', 'admin@example.com')
#guest = User1('guest', 'guest@example.com')

#db.session.add(admin)
#db.session.add(guest)
#db.session.commit()    
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host = "127.0.0.1", port = 5000)