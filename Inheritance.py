# class Employee:
#     company="Google"
#     def showDetails(self):
#         print("this is an employee")

# class Programmer(Employee):
#     language="python"
#     company="facebook"
#     def getLanguage(self):
#         print(f"The language is {self.language}")

# e=Employee()
# e.showDetails()
# s=e.company
# print(s)
# p=Programmer()
# p.showDetails()
# print(p.company) #first search in our class than other

#one class to create anoter class
class C_2d:
    def __init__(self,a,b):
        a=str(a)+"i"
        b=str(b)+"j"
        print(a,"+",b,"+",end=" ")

class C_3d:
    def __init__(self,c):
        super().__init__()
        c=str(c)
        print(c,"k")

a=C_2d(1,2)
b=C_3d(3)

#animal class
class Animal:
    animalType="mammal"
class Pet(Animal):
    pet="dog"
class Dog(Pet):
    @staticmethod
    def bark():
        print("bow bow!")

d=Dog()
d.bark()
print(d.pet)
print(d.animalType)