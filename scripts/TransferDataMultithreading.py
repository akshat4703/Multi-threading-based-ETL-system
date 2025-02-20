import mysql.connector
import threading
import time

def transfer_chunk(rows):
    conn = mysql.connector.connect(host="localhost", user="root", password="password", database="etl_db")
    cursor = conn.cursor()

    for row in rows:
        cursor.execute("INSERT INTO destination_table (name, age) VALUES (%s, %s)", (row[1], row[2]))
        conn.commit()

    cursor.close()
    conn.close()

def multithreading_transfer():
    conn = mysql.connector.connect(host="localhost", user="root", password="password", database="etl_db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM source_table")
    rows = cursor.fetchall()

    num_threads = 4  # Number of threads
    chunk_size = len(rows) // num_threads
    threads = []

    start_time = time.time()

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread = threading.Thread(target=transfer_chunk, args=(rows[start:end],))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Multithreading Transfer Time: {end_time - start_time:.4f} seconds")

    cursor.close()
    conn.close()

multithreading_transfer()
