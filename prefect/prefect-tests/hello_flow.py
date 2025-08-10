from prefect import flow

@flow
def hello_world():
    print('hello_world')


hello_world()