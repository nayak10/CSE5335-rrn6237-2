# CSE 5335 - Project 2
##### - Rajesh R Nayak (rrn6237)



### External data source used to populate your Heroku data sources

The data source has been taken from the following website
```sh
https://datahub.io/dataset/fifa-world-cup-2014-all-players
```
- This data is for all the soccer player from 2014 FIFA world cup. Only some data has been selected and used, since only 100 tuples were required for the project.
- The data was uploaded to Postgresql using the 'Insert into table' commands by accessing the Heroku Postgres on PSQL SQL Shell
- The primary key 'PlayerID' has been updated automatically by running a loop. 
The player ratings are randomly assigned float values between 6 and 10.

### Heroku toolbelt commands to execute the scripts

The commands have been run from the GIT CMD command line interface.
- Commands used to upload to GitHub
     - **git init**
     - **heroku git:remote -a CSE5335-rrn6237-2**
     - **git remote -v**
     - **git add .**
     - **git commit -m "Version Name"**
     - **git push heroku master**
     - **heroku run bash**
- Command to run the python scripts **python <script_name.py>**
- In some cases, packages have to be installed under bash before running the python program. For example,
    - pip install redis
    - pip install pymongo

### Aspects of implementation which were easy 

- Python supports inbuilt packages for MongoDB (pymongo) and Redis (Redis-py) which made it easy to configure the application.
- The Postgres was the easiest to use, since I was already familiar with Relational Databases.

### Aspects of implementation which were hard

- The documentation for Heroku Redis and Heroku MongoLabs to integrate with Python is very limited. Hence, a lot of research had to be done to understand the flow of the application
- Since I had no experience working on Heroku, I had to spend lot of time configuring it to work with Github and to access it.
