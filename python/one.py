from time import sleep

from celery import Celery

app = Celery('one', broker="redis://127.0.0.1", backend="redis://127.0.0.1")

app.config_from_object('conf')


@app.task
def add(x, y):
    return x + y


@app.task()
def sub(x, y):
    return x - y


# result = add.signature((3, 4))
# result.delay()

###########################

# result = add.apply_async((6, 1), link=sub.signature((5,)))
###########################

# result = add.apply_async((6, 1), link=sub.signature((5, 4), immutable=True))
# result = add.apply_async((6, 1), link=sub.si(5, 4))

###########################