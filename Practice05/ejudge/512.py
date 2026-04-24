import re
s = input()
ans = re.findall("[0-9]{2,}", s)
for i in ans:
    print(i, end=" ")