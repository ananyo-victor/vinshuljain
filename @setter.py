# class Employee:
#     company="Barat Gas"
#     salary=20000
#     bonus=1000
#     # totalSalary=20000
#     @property
#     def totalSalary(self):
#         return self.salary + self.bonus
#     @totalSalary.setter
#     def totalSalary(self,val):
#         self.bonus=val-self.salary #it change bonus value

# e=Employee()
# print(e.totalSalary)
# e.totalSalary=25000
# print(e.salary)
# print(e.bonus)

class Employee:
    salary=100
    increment=100
    @property
    def salaryAfterincrement(self):
        return self.salary + self.increment
    @salaryAfterincrement.setter
    def salaryAfterincrement(self,val):
        self.increment=val-self.salary
        return self.increment
f=Employee()
print(f.increment)
print(f.salaryAfterincrement)
f.salaryAfterincrement=400
print(f.increment)