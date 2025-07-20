from airflow.sdk import dag, task


@dag
def branch_dag():

    @task
    def a() -> int:
        return 0
    
    @task.branch
    def b(val: int):
        if val == 1:
            return 'equal_1'
        return 'different_than_1'
    
    @task
    def equal_1():
        print('Equal to one')

    @task
    def different_than_1():
        print('Different than one')

    val = a()
    b(val) >> [equal_1(), different_than_1()]

branch_dag()

    