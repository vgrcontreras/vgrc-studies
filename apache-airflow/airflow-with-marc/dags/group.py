from airflow.sdk import dag, task, task_group

@dag
def my_dag():

    @task
    def a():
        print('a')

    @task_group
    def my_group():
        @task
        def b():
            print('b')

        @task_group
        def my_nested_group():

            @task
            def c():
                print('c')
                
            c()

        b() >> my_nested_group()

    a() >> my_group()

my_dag()