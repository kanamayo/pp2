import re
s = input().split()
found = 0
for i in s:
    if re.search("\S+@\S+\.\S+", i):
        print(i)
        found = True
        break
if found == False:
    print("No email")