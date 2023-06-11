import psycopg2
from dotenv import load_dotenv , dotenv_values

CONFIG = dotenv_values(".env") 

conn = psycopg2.connect(
    database = CONFIG.get("DATABASE_NAME") , 
    user =CONFIG.get("DATABASE_USER") , 
    host= CONFIG.get("DATABASE_HOST") , 
    password = CONFIG.get("DATABASE_PASSWORD") , 
    port = int(CONFIG.get("DATABASE_PORT")) , 
)

cur = conn.cursor() 
# Execute a query
cur.execute("SELECT * FROM food_items")

# Retrieve query results
records = cur.fetchall()

for record in records :
    print(record)

#create table 
cur.execute(
    "CREATE table IF NOT EXISTS pgtest(id SERIAL PRIMARY KEY , name VARCHAR(30) NOT NULL);"
) 

cur.execute("INSERT INTO pgtest VALUES(%s,%s)" , (1 , "John Dove"))
#insert into table  
conn.commit()
cur.close() 
conn.close() 