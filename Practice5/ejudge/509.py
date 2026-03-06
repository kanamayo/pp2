import re
s = input()
a = re.split(" ", s)
ans = 0
for i in a:
    print(i)
    if len(i) == 3:
        ans += 1
# a = re.findall(".{3}", s)
print("-"*10)
print(ans)