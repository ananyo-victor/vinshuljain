class Person:
    country="India"
    def __init__(self):
        print("I am class person")
    def takeBreath(self):
        print("I am breathing")

class Employee(Person):
    compony="Honda"
    def __init__(self):
        super().__init__()
        print("I am class employee")
    def getSalary(self):
        print(f"salary is {self.salary}")
    def takeBreath(self):
        super().takeBreath()
        print("I am employ and luckilly i am breating")

class Programmer(Employee):
    company="filverr"
    def __init__(self):
        super().__init__()
        print("I am class programmer")
    def getSalary(self):
        print("no salary to programmer")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am programmer and i am breathing")

per=Person()
per.takeBreath()

e=Employee()
e.takeBreath()

p=Programmer()
p.takeBreath()
