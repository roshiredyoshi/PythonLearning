import datetime as dt

def record_time(message, time = dt.datetime.now()):
    print("{:}, time: {:}".format(message,time))

record_time("It is the morning")
record_time("It is the morning", "Feb 22")
