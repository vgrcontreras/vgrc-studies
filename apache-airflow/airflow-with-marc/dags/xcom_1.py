from airflow.sdk import dag, task, Context

@dag
def xcom_dag1():
    
    @task
    def t1() -> int:
        val = 42
        return val

    @task
    def t2(val: int):
        print(val)

    val = t1()
    t2(val)

xcom_dag1()