import os 
from dotenv import load_dotenv 
import psycopg2


load_dotenv()

# Get data from env
DBNAME = os.getenv("DBNAME")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

# Create connection
conn = psycopg2.connect(
    dbname=DBNAME,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
)

# Create cursor
cur = conn.cursor()

# Query
cur.execute("SELECT version();")
# Get result from cursor
result = cur.fetchone()
print(result)


# Finally
cur.close()
conn.close()
