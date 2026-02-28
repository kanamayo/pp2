class Reverse:
    def __init__(self, s):
        self.string = s
    def Reverse(self):
        ret = self.string[::-1]
        return ret
    
i = input()
obj = Reverse(i)
ans = obj.Reverse
for i in ans:
    print(i, end="")
# print(ans)