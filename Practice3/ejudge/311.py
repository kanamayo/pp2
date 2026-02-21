class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sum(self, pair2):
        a_sum = int(self.a) + int(pair2.a)
        b_sum = int(self.b) + int(pair2.b)
        print(f"Result: {a_sum} {b_sum}")
inn = input().split()
a1, b1, a2, b2 = inn[0], inn[1], inn[2], inn[3]
obj1 = Pair(a1, b1)
obj2 = Pair(a2, b2)
obj1.sum(obj2)