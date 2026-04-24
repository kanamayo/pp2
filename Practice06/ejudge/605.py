s = input()
ans = any(x == 'a' or x == 'i' or x == 'u' or x == 'e' or x == 'o' for x in s.lower())
if ans:
    print("Yes")
else:
    print("No")