import mysql.connector
import time

def one_by_one_transfer():
    conn = mysql.connector.connect(host="localhost", user="root", password="password", database="etl_db")
    cursor = conn.cursor()

    # Fetching data
    cursor.execute("SELECT * FROM source_table")
    rows = cursor.fetchall()

    start_time = time.time()
    
    # Inserting each row one by one
    for row in rows:
        cursor.execute("INSERT INTO destination_table (name, age) VALUES (%s, %s)", (row[1], row[2]))
        conn.commit()
    
    end_time = time.time()
    print(f"One-by-One Transfer Time: {end_time - start_time:.4f} seconds")

    cursor.close()
    conn.close()

one_by_one_transfer()
