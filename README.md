# basic-docker-etl-project

DOCUMENTAIION FOR THIS PROJECT

1. PROJECT HIERACHY
  app
    generate_data.py
    load.py
    main.py
    extract.py
    transform.py
    requirements.py
  sql
    init.py
  Dockerfile
  docker-compose.yml

2. SETUP docker-compose.yml

version: '3'
services:
  postgres:
    image:postgres:15
    container_name: postgres
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: postgres-db
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./sql/init.sql:/docker-entrypoint-initdb.d/init.sql
  etl:
    build: .
    container_name: etl-pipeline
    depends-on:
      - postgres
volumes:
  postgres-data:

3. Dockerfile

FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN mkdir -p data
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","main.py"]

4. requirements.txt
   pandas
   numpy
   psycopg2-binary
   sqlalchemy
5. main.py
   - this file includes extract, transform , load function from their files.
   - include connection of postgresql
       conn = psycopg2.connect(
           host = os.getenv("POSTGRES_HOST"),
           user = os.getenv("POSTGRES_USER"),
           password = os.getenv("POSTGRES_PASSWORD"),
           database = os.getenv("POSTGRES_DB),
           host=5432
       )
   - this file will use the functionality of check db which connected by using try...except and time.sleep()
     for i in range(10):
         try:
               conn = psycopg2.connect(
                   host = os.getenv("POSTGRES_HOST"),
                   user = os.getenv("POSTGRES_USER"),
                   password = os.getenv("POSTGRES_PASSWORD"),
                   database = os.getenv("POSTGRES_DB),
                   host=5432
               )
           except Exception as e:
               print(f"error when connecting...{e}")
               time.sleep(5)
  if __name__ == "__main__":
      wait_connection()
6. generate_data
   get code dummy data from chatgpt because it is not important than docker and ETL pipeline
   df.to_csv("data/order_dirty.csv")
7. extract.py
   pd.read_csv("data/order_dirty.csv")
8. transform.py
   a. drop null values dropna(subnet=)
   b. change datatype pd.to_datetime, pd.to_numeric, astype(int)
   c. business logic fillna('unknown')
   d. drop duplicates df.drop_duplicates()
9. load
     curr = conn.cursor()
     with open("data/orders_clean.csv","r") as f
     curr.copy_expert(
        COPY orders_clean FROM STDIN WITH CSV HEADER
     ,f)

     conn.commit()
     curr.close()
9. CMD commands
     a. docker compose up --build
     b. docker compose down -v
     c. docker ps
     d. docker images
     e. docker rmi image_name
     f. docker rm container_name
     g. docker stop container_name
     h. docker exec -it container_name psql -u admin -d postgres-db
10. APACHE AIRFLOW
  a. docker-compose.yml

  airflow:
    image:apache/airflow:2.9.0
    container_name:airflow
    restart:always
    environment:
      - AIRFLOW__CORE__LOAD_EXAMPLES=False
    ports:
      - "8080:8080"
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
    command: >
      bash -c "airflow db init && airflow users create --username admin --password admin --firstname admin --lastname admin --email admin@example.com --roie Admin && airflow webserver & airflow scheduler
11, etl-pipeline.py
  from airflow import DAG
  from airflow.operators.bash import BashOperator
  from datetime import datetime


  with DAG(
    dag_id="etl_pipeline"
    date_time=datetime(2026,4,1),
    schedule_interval="@daily",
    catchup=False
  ) as dag:
       generate = BashOperator(
         task_id="generate",
         bash_command="python generate.py"
       )
       extract = BashOperator(
         task_id="extract",
         bash_command="python extract.py"
       )
       transform = BashOperator(
         task_id="transform",
         bash_command="python transform.py"
       )
       load = BashOperator(
         task_id="load",
         bash_command="python load.py"
       )
       generator >> extract >> transform >> load
   
             

    

