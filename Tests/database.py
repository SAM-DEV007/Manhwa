import psycopg2
import os

from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

if __name__ == '__main__':
    with open(Path(__file__).parent.resolve() / 'manhwa.json', 'r') as f:
        data = f.read()

    with psycopg2.connect(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE_NAME')
    ) as conn:

        conn.autocommit = True

        cursor = conn.cursor()

        # cursor.execute('CREATE TABLE Manhwa (id SERIAL PRIMARY KEY, data JSONB)')
        # cursor.execute('INSERT INTO Manhwa (data) VALUES (%s)', (data,))

        cursor.execute('SELECT * FROM Manhwa')
        print(cursor.fetchall())
        
