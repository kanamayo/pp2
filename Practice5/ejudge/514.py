import re
s = input()
t = re.compile("^\d+$")
print(s)
print(str(t))
if re.search(t, s):
    print("Match")
else:
    print("No match")