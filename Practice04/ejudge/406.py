def f(n):
    prevprev = 0
    prev = 0
    cur = 0
    yield cur
    for i in range(0, n - 1):
        # print(i, cur, prev, prevprev)
        if i == 0:
            cur = 1
            yield cur
        else:
            temp = cur
            cur = cur + prev
            prev = temp
            yield cur

j = int(input())
if j != 0:
    k = f(j)
    f(j)
    o = 0
    for i in k:
        print(i, end="")
        if o >= j - 1:
            break
        o += 1
        print(',', end="")