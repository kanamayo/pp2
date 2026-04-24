import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"({self.x}, {self.y})")
    def dist(self, x2, y2):
        ans = math.sqrt(((x2 - self.x)**2) + ((y2 - self.y)**2))
        print(f"{ans:.2f}")
inn = input().split()
xi, yi = int(inn[0]), int(inn[1])
point1 = Point(xi, yi)
point1.show()
inn = input().split()
xi, yi = int(inn[0]), int(inn[1])
point1.move(xi, yi)
inn = input().split()
xi, yi = int(inn[0]), int(inn[1])
point1.dist(xi, yi)