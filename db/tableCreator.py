import psycopg2
import logging

try:
    conn = psycopg2.connect(host="localhost", dbname="finances_db", user="root", password="mysecretpass", port=5432)
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Finances(
                id SERIAL PRIMARY KEY,  
                transaction_name VARCHAR(50),
                shop_name VARCHAR(100),
                city VARCHAR(50),
                country VARCHAR(50),
                amount FLOAT,
                currency_ISO VARCHAR(3),
                date TIMESTAMP,
                category VARCHAR (30),
                type VARCHAR(4), --card or cash
                notes TEXT
    );
    """)
except psycopg2.OperationalError as e:
    raise ConnectionError(f"Couldn't connect to database: {e}")

except psycopg2.DatabaseError as e:
    logging.error(f"Database structure error: {e}")

except Exception as e:
    logging.error(f"Unexpected error: {e}")

finally:
    if conn:
        conn.commit()
        cur.close()
        conn.close()