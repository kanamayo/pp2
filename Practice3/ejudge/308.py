class Account:
    def __init__(self, balance):
        self.balance = balance
    def withdrawal(self, w):
        if self.balance < w:
            print("Insufficient Funds")
        else:
            print(self.balance - w)
inn = input().split()
a, b = int(inn[0]), int(inn[1])
obj1 = Account(a)
obj1.withdrawal(b)