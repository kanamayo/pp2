import re
s = input()
if re.findall("^\D", s) and re.findall("\d$", s):
    print("Yes")
else:
    print("No")

# print(re.findall('\d', s))