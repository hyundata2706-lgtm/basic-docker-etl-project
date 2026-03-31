import os
import psycopg2
import time

def wait_connection():
  for i in range(5):
    try:
      conn = psycopg2.connect(
        host=os.getenv("POSGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
        port=5432
      )
      print("ETL is running")
      return conn
    except Exception as e:
      print(f"error when connecting.. {e})
      time.sleep(5)


if __name__ = "__main__":
  wait_connection()
