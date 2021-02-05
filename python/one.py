from  time import sleep

from celery import Celery

app = Celery('one', broker="amqp://localhost")


@app.task
def add(x, y):
    sleep(15)
    return x + y