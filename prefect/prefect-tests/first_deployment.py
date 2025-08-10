from prefect import task, flow


@task
def hello_message():
    msg = 'hello_world'
    return(msg)


@flow
def first_deployment():
    task_message = hello_message()
    print(task_message)


first_deployment.serve(name='my_first_deployment')