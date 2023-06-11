# py-flask
Lessons on Flask and how to build API using Python

## Connecting to a Database 

Install the psycopg-binary package for testing and developing. 

$ source venv/bin/activate
$ python3 -m pip install psycopg2-binary python-dotenv 

The psycop2 library is to enable us connect to postgresql , 
while the python-dotenv is to allow us be able to load environment 
varibles stored within a .env file at the root of our directory