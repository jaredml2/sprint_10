#Step 0 - import sqlite3
import sqlite3
import queries as q
import pandas as pd
#DB connect function 
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    #make the cursor
    curs = conn.cursor()
    #execute the query
    curs.execute(query)
    #pull and return the results
    return curs.fetchall()
#step 1
#connect to the database. TRIPLE CHECK SPELLING OF DB FILE NAME
# the below line is replaced by the def connnect_to_db line
# connection = sqlite3.connect('rpg_db.sqlite3')

#step 2 - make the "cursor"
#cursor = connection.cursor()

#step 3 - write a query 
#see queries.py file 

#step 4 - execute the query on the cursor and fetch the results 
#'pulling the results' from the cursor 
#results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    conn = connect_to_db()
    print(execute_q(conn, q.SELECT_ALL)[:5])
    results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    df = pd.DataFrame(results)
    df.columns = ['name', 'average_item_weight']
    print(df.head())
    df.to_csv('rpg_db.csv', index=False)