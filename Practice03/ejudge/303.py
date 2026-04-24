s = input()
n1 = 0
n2 = 0
if s.count('+') == 1:
    mult = s.index('+')
    operation = "+"
if s.count('-') == 1:
    mult = s.index('-')
    operation = "-"
if s.count('*') == 1:
    mult = s.index('*')
    operation = "*"
l = len(s)
ten = mult // 3 - 1
for i in range(0, mult):
    a = s[i]
    b = s[i + 1]
    c = s[i + 2]
    num = False
    if a == ' ' or b == ' ' or c == ' ':
        continue
    if a == 'O' and b == 'N' and c == 'E':
        n1 += 1 * (10**ten)
        num = True
    if a == 'T':
        if b == 'W' and c == 'O':
            n1 += 2 * (10**ten)
            num = True
        elif b == 'H' and c == 'R':
            n1 += 3 * (10**ten)
            num = True
    if a == 'F':
        if b == 'O' and c == 'U':
            n1 += 4 * (10**ten)
            num = True
        elif b == 'I' and c == 'V':
            n1 += 5 * (10**ten)
            num = True
    if a == 'S':
        if b == 'I' and c == 'X':
            n1 += 6 * (10**ten)
            num = True
        elif b == 'E' and c == 'V':
            n1 += 7 * (10**ten)
            num = True
    if a == 'E' and b == 'I' and c == 'G':
        n1 += 8 * (10**ten)
        num = True
    if a == 'N' and b == 'I' and c == 'N':
        n1 += 9 * (10**ten)
        num = True
    if a == 'Z' and b == 'E' and c == 'R':
        num = True
    if num:
        ten -= 1
        i += 2
    # print (a, b, c, " ", i, i + 1, i + 2, " ", num, ten , mult, " ", n1)

ten = int((len(s) - mult) // 3) - 1
# print('-' * 26)
for i in range(mult + 1, l):
    if i >= l or i + 1 >= l or i + 2 >= l:
        break
    a = s[i]
    b = s[i + 1]
    c = s[i + 2]
    num = False
    if a == ' ' or b == ' ' or c == ' ':
        continue
    if a == 'O' and b == 'N' and c == 'E':
        n2 += 1 * (10**ten)
        num = True
    if a == 'T':
        if b == 'W' and c == 'O':
            n2 += 2 * (10**ten)
            num = True
        elif b == 'H' and c == 'R':
            n2 += 3 * (10**ten)
            num = True
    if a == 'F':
        if b == 'O' and c == 'U':
            n2 += 4 * (10**ten)
            num = True
        elif b == 'I' and c == 'V':
            n2 += 5 * (10**ten)
            num = True
    if a == 'S':
        if b == 'I' and c == 'X':
            n2 += 6 * (10**ten)
            num = True
        elif b == 'E' and c == 'V':
            n2 += 7 * (10**ten)
            num = True
    if a == 'E' and b == 'I' and c == 'G':
        n2 += 8 * (10**ten)
        num = True
    if a == 'N' and b == 'I' and c == 'N':
        n2 += 9 * (10**ten)
        num = True
    if a == 'Z' and b == 'E' and c == 'R':
        num = True
    if num:
        ten -= 1
    # print (a, b, c, " ", i, i + 1, i + 2, " ", num, ten , mult, len(s), " ", n2)
# print(n1, n2)
match operation:
    case '*':
        ans = n1 * n2
    case '+':
        ans = n1 + n2
    case '-':
        ans = n1 - n2
# print(ans)
anss = []
while ans:
    i = int(ans % 10)
    if i == 1: anss.append("ONE")
    if i == 2: anss.append("TWO")
    if i == 3: anss.append("THR")
    if i == 4: anss.append("FOU")
    if i == 5: anss.append("FIV")
    if i == 6: anss.append("SIX")
    if i == 7: anss.append("SEV")
    if i == 8: anss.append("EIG")
    if i == 9: anss.append("NIN")
    if i == 0: anss.append("ZER")  
    ans = int(ans / 10)
for i in range(0, len(anss)):
    print(anss[len(anss) - 1 - i],end="")