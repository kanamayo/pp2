n = int(input())
d = {}
for i in range(0, n):
    inp = input().split()
    name = inp[0]
    if (name not in d):
        d[name] = 0
        d[name] += int(inp[1])
    else:
        d[name] += int(inp[1])
for i in sorted(d):
    print(f"{i} {d[i]}")