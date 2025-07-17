from airflow.sdk import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sensors.base import PokeReturnValue
from airflow.providers.postgres.hooks.postgres import PostgresHook


@dag
def user_processing():
    
    create_table = SQLExecuteQueryOperator(
        task_id='create_table',
        conn_id='postgres',
        sql="""
        CREATE TABLE IF NOT EXISTS users (
            id INT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


    @task.sensor(poke_interval=30, timeout=300)
    def is_api_available() -> PokeReturnValue:
        import requests

        response = requests.get('https://raw.githubusercontent.com/marclamberti/datasets/refs/heads/main/fakeuser.json')

        if response.status_code == 200:
            condition = True
            fake_user = response.json()
        else:
            condition = False
            fake_user = None

        return PokeReturnValue(is_done=condition, xcom_value=fake_user)
    

    @task
    def extract_user(fake_user):
        return {
            "id": fake_user['id'],
            "first_name": fake_user['personalInfo']['firstName'],
            "last_name": fake_user['personalInfo']['lastName'],
            "email": fake_user['personalInfo']['email']
        }
    

    @task
    def process_user(user_info):
        import csv
        from datetime import datetime

        user_info["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open('/tmp/user_info.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=user_info.keys())
            writer.writeheader()
            writer.writerow(user_info)

    @task
    def store_user():
        hook = PostgresHook(postgres_conn_id='postgres')
        hook.copy_expert(
            sql='COPY users FROM STDIN WITH CSV HEADER',
            filename='/tmp/user_info.csv'
        )

    process_user(extract_user(create_table >> is_api_available())) >> store_user()


user_processing()