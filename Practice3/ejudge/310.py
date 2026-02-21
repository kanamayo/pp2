class Person:
    def __init__(self, name):
        self.name = name
    def area(self):
        ans = 3.14159 * self.radius**2
        print(f"{ans:.2f}")
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")
inn = input().split()
a, b = inn[0], inn[1]
obj1 = Student(a, b)
obj1.display()