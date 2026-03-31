CREATE TABLE orders_clean(
  id INT PRIMARY KEY,
  user_id INT,
  order_date TIMESTAMP,
  amount FLOAT,
  status VARCHAR(20)
)
