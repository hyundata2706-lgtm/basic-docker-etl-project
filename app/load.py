def load_db(conn):
  curr = conn.cursor()
  with open("data/order_clean","r") as f
  curr.copy_expert(
    "COPY orders_clean FROM STDIN WITH CSV HEADER",f
  )
  conn.commit()
  curr.close
  print("loaded data into postgres-db)
