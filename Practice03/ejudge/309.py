class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        ans = 3.14159 * self.radius**2
        print(f"{ans:.2f}")
a = int(input())
obj1 = Circle(a)
obj1.area()