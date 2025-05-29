import sqlite3
import os

def setup():
    schema_path = os.path.join("lib", "db", "schema.sql")
    if not os.path.exists(schema_path):
        print("Schema file not found at", schema_path)
        return
    with open(schema_path) as f:
        schema = f.read()
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("Database schema created.")

if __name__ == "__main__":
    setup()