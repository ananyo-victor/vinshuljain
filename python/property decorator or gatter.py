class Employee:
    company="Barat pay"
    salary=20000
    bonus=1000
    # totalSalary=20000
    @property
    def totalSalary(self):
        return self.salary + self.bonus

e=Employee()
print(e.totalSalary)