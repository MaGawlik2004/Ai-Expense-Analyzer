import psycopg2
import logging
import random
from data_config import country

try:
    conn = psycopg2.connect(host="localhost", dbname="finances_db", user="root", password="mysecretpass", port=5432)
    cur = conn.cursor()

except Exception as e:
    logging.error(f"Unexpected Error: {e}")

finally:
    if conn:
        conn.commit()
        cur.close()
        conn.close()
