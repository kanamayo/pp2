import math
n = int(input())
innums = input().split()
arr = [int(i) for i in innums]
q = int(input())
while q:
    inp = input().split()
    a = inp[0]
    if a != "abs": b = int(inp[1])
    if a == "abs":
        arr = list(map(lambda i: abs(i), arr))
    elif a == "multiply":
        arr = list(map(lambda i: i * b, arr))
    elif a == "power":
        arr = list(map(lambda i: i ** b, arr))
    elif a == "add":
        arr = list(map(lambda i: i + b, arr))
    
    q -= 1
for i in arr:
    print(i, end = " ")