import re
def f(a):
    # print(a)
    # print(str(a) * 2)
    return a.group() * 2
s = input()
# digits = re.findall("\d", s)
ans = re.sub("\d", f, s)
print(ans)