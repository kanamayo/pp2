import datetime

inn = int(input("Days ago: "))
a = datetime.datetime.now()
b = a - datetime.timedelta(days=inn)

c = a - b
ans = c.total_seconds()

print("Difference in seconds:", ans)