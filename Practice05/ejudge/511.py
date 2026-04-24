import re
s = input()
ans = re.findall("[A-Z]", s)
print(len(ans))