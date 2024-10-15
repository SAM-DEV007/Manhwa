import psycopg2
import os

from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    with open(Path(__file__).parent.resolve() / 'manhwa.json', 'r') as f:
        data = f.read()

    with psycopg2.connect(
        host=os.getenv('DBHOST'),
        port=os.getenv('DBPORT'),
        user=os.getenv('DBUSER'),
        password=os.getenv('DBPASSWORD'),
        database=os.getenv('DATABASE_NAME')
    ) as conn:

        conn.autocommit = True

        cursor = conn.cursor()

        cursor.execute('CREATE TABLE home_manhwa (id SERIAL PRIMARY KEY, data JSONB)')
        cursor.execute('INSERT INTO home_manhwa (data) VALUES (%s)', (data,))

        cursor.execute('SELECT * FROM home_manhwa')
        print(cursor.fetchall())
        
