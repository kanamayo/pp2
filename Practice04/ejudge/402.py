j = int(input())
if j == 0 or j == 1:
    print(0)
else:
    for i in range(0, j + 1, 2):
        print(i, end="")
        if i == (j - (j % 2)):
            break
        print(',', end='')