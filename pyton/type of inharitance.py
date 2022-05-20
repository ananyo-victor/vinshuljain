'''
1.single inharitance
2.multiple inharitance
3.multi-level inharitance
'''
#single inharitance
class Employee:
    company="Google"
    def showDetails(self):
        print("this is an employee")

class Programmer(Employee):
    language="python"
    company="facebook"
    def getLanguage(self):
        print(f"The language is {self.language}")

e=Employee()
e.showDetails()
s=e.company
print(s)
p=Programmer()
p.showDetails()
print(p.company)

#mutiple inharitance
class A:
    def showDetails(self):
        print("this is class a")

class B:
    def display(self):
        print("this is class b")

class C(A, B):
    def __init__(self):
        print("this is class c")

object=C()
object.showDetails()
object.display()

# multi-level inharitance
class A:
    def showDetails(self):
        print("this is class a")

class B(A):
    def display(self):
        print("this is class b")

class C(B):
    def __init__(self):
        print("this is class c")

object=C()
object.showDetails()
object.display()