from prefect import task, flow


@task
def hello_message():
    msg = 'hello_world'
    return(msg)


@flow
def main():
    task_message = hello_message()
    print(task_message)


main()