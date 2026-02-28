import datetime

a = datetime.datetime.now()
b = a.replace(microsecond=0)
print("Drop microseconds:", b)