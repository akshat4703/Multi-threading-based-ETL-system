import pandas as pd
import mysql.connector
import time

def import_export_transfer():
    conn = mysql.connector.connect(host="localhost", user="root", password="Akshat@4703", database="etl_db")
    cursor = conn.cursor()

    start_time = time.time()

    # Export to CSV
    df = pd.read_sql("SELECT * FROM source_table", conn)
    df.to_csv("data.csv", index=False)

    # Import from CSV
    df = pd.read_csv("data.csv")
    for index, row in df.iterrows():
        cursor.execute("INSERT INTO destination_table (name, age) VALUES (%s, %s)", (row["name"], row["age"]))
        conn.commit()

    end_time = time.time()
    print(f"Import/Export Transfer Time: {end_time - start_time:.4f} seconds")

    cursor.close()
    conn.close()

import_export_transfer()
