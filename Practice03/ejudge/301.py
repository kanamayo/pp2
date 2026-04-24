def func(num):
    while int(num):
        i = int(num % 10)
        print(i)
        if i % 2 == 1:
            return False
            break
        num /= 10
    return True
n = int(input())
if func(n) == True:
    print("Valid")
else:
    print("Not valid")
