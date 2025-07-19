from airflow.sdk import dag, task, Context
from typing import Any

"""
This DAG is used to apply the concept of returning multiple values with X-COM
"""

@dag
def xcom_dag2():
    
    @task
    def t1() -> dict[str, Any]:
        return {
            'value1': 42,
            'value2': 'hello world'
        }

    @task
    def t2(data: dict[str, Any]):
        print(data['value1'])
        print(data['value2'])

    data = t1()
    t2(data)

xcom_dag2()