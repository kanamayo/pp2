innums = input().split()
n = [int(i) for i in innums]

def func(k):
    if k == 1 or k == 0: return False
    for i in range (2, k):
        if k % i == 0:
            return False
    return True
ans = list(filter(func, n))
if not ans:
    print("No primes")
for i in ans:
    print(i, end = " ")