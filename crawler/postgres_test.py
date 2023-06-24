from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import psycopg2


def interact_with_postgres():
    conn = psycopg2.connect(database="OLX", user="postgres", password="123456789", host="postgres", port="5432")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS test_table;")
    conn.commit()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS test_table (
                    id SERIAL PRIMARY KEY,
                    value VARCHAR(255)
                );
                ''')
    cur.execute("INSERT INTO test_table (value) VALUES ('data');")
    conn.commit()
    cur.close()
    conn.close()


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 6, 22),
}

with DAG('test_postgres_dag_2',
         default_args=default_args,
         description='A simple postgres test dag',
         schedule_interval='0 0 * * *',
         ) as dag:

    t1 = PythonOperator(
        task_id='interact_with_postgres',
        python_callable=interact_with_postgres,
    )
