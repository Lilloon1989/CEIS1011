#Purpose: Query database using SQL
#Name: Your name
#Date: Your date
#   Run BuildWeatherDB.py to build weather database before running this program

import sqlite3
import pandas as pd


#file names for database and output file
dbFile = "weather.db"

#format output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#connect to and query weather database 
conn = sqlite3.connect(dbFile)
#Create SQL command
selectCmd1 = " SELECT * FROM observations ORDER BY timestamp; "
selectCmd2 = " SELECT MIN(temperature), MAX(temperature) FROM observations; "                
                
#print out the query
result1 = pd.read_sql_query(selectCmd1, conn)
result2 = pd.read_sql_query(selectCmd2, conn)
print(result1)
