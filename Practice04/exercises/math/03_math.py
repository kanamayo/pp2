import math
s = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
a = (s * (l**2)) / (4 * math.tan(math.radians(180 / s)))
print(f"The area of the polygon is: {a:.2f}")
