import datetime

a = datetime.datetime.now().date()
print("Yesterday:", int(a.strftime("%d")) - 1)
print("Today:", int(a.strftime("%d")))
print("Tomorrow:", int(a.strftime("%d")) + 1)