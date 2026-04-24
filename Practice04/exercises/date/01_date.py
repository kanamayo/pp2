import datetime

a = datetime.datetime.now()

print("Current date:", int(a.strftime("%d")))
print("5 days ago:", int(a.strftime("%d")) - 5)