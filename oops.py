class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def getSalary(self):
        print(self.salary)

shoaib=Employee("shoaib","100000000")
print(shoaib.salary)
print(shoaib.name)
shoaib.getSalary()