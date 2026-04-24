import re
s = input()
t = re.search("Name: (.+), Age: (.+)", s)
if t:
    a, b = t[1], t[2]
    print(a, b)