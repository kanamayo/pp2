class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = int(base_salary)
    def total_salary(self):
        print(f"Name: {self.name}, Total: {self.base_salary:.2f}")
class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        self.name = name
        self.base_salary = int(base_salary) * (1 + int(bonus_percent) / 100)
class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        self.name = name
        self.base_salary = int(base_salary) + (int(completed_projects) * 500)
inn = input().split()
a, b, c = inn[0], inn[1], inn[2]
if a == "Manager" or a == "Developer":
    d = inn[3]
if a == "Manager":
    obj1 = Manager(b, c ,d)
elif a == "Developer":
    obj1= Developer(b, c, d)
else:
    obj1 = Employee(b, c)
obj1.total_salary()