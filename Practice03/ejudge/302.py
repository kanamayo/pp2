def isUsual(a):
    num = int(a)
    while num:
        print(num)
        if num == 1:
            return True
        elif int(num % 2) == 0:
            num /= 2
        elif int(num % 3) == 0:
            num /= 3
        elif int(num % 5) == 0:
            num /= 5
        else:
            return False
    return True

n = int(input())
if isUsual(n):
    print("Yes")
else:
    print("No")