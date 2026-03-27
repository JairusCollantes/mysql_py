import mysql.connector
from dotenv import load_dotenv
load_dotenv()

con =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "jairus",
    database = "playlist_db"
)
print("con")   