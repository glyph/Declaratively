from declog import log_messages

with log_messages.declarations() as l:
    hello_world = l.declare("%s, world!")
    goodbye_world = l.declare("%s, world.")


def log_something():
    hello_world.warning("hello, %s")
    goodbye_world.warning("goodbye, %(more data)s")


def whoops():
    with log_messages.declarations() as error:
        oops = error.declare("but I just want one more log message...")
    oops.warning("nope")


log_something()

whoops()
