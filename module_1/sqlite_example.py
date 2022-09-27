#Step 0 - import sqlite3
import sqlite3
import queries as q

#step 1
#connect to the database. TRIPLE CHECK SPELLING OF DB FILE NAME
connection = sqlite3.connect('rpg_db.sqlite3')

#step 2 - make the "cursor"
cursor = connection.cursor()

#step 3 - write a query 
#see queries.py file 

#step 4 - execute the query on the cursor and fetch the results 
#'pulling the results' from the cursor 
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
