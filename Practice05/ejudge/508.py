import re
s = input()
r = input()
a = re.split(r, s)
for i in range(0, len(a)):
    print(a[i], end="")
    if i != len(a) - 1:
        print(",", end="")