# # before using class method (class attribute not change)
# class Employee:
#     company="camal"
#     salary=100
#     location="delhi"

#     def changeSalary(self,sal):
#         self.salary=sal

# e=Employee()
# print(e.salary)
# e.changeSalary(400)
# print(e.salary)
# print(Employee.salary)

# after using class method(class attributed also change)
class Employee:
    company="camal"
    salary=100
    location="delhi"

    def changeSalary(self,sal):
        self.__class__.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(400)
print(e.salary)
print(Employee.salary)

'''or we can do this by one more method'''

class Employee:
    company="camal"
    salary=200
    location="delhi"
    @classmethod
    def changeSalary(cla,sal):
        cla.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(400)
print(e.salary)
print(Employee.salary)