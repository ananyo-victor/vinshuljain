#it is return in oop parton
class Sum:          # class name always witen in pascal case
    def sum(self):   #in case of self we can write any other name but self is a stander form so we always write self
        return self.a+self.b 
k=Sum() #inshalisation of object of class Sum   #it is an instance of class
k.a=12
k.b=13
s=k.sum()
print(s)
'''
PascalCase:
            EmployName #example of pascalCase
camelCase:-
            isNameDefineByUser #example of camelCase
'''
#some more example of class with the help of oop
class RailwayForm:
    formtype="Railway form"
    def printData(self, signature):    #self:- it is a parameter which pass atomatically
        print("name in form is",self.a) #self.a :- parameter given at the instance of class
        print("name of train is",self.b,"\n",signature)
    @staticmethod
    def greet():    #run without using self statement
        print("Good Morning, Sir")

data=RailwayForm()
data.a="vinshul"
data.b="shanti express"
data.printData("thanks!") #to use parameter at the time of exicution ,note:- self should be use
# data.printData() # same as:- RailwayForm.printData(data)
data.greet()
# changing the class attributed(things which are directly link with class are called class attributed
# )
class Employ:
    company="Instagram"
    salary=100

tina=Employ()
vinshul=Employ()
print(tina.company)
print(vinshul.company)
print(tina.salary)
print(vinshul.salary)

Employ.company="Facebook"
tina.salary=300    #instance attribute
vinshul.salary=400    #instance attribute
print(tina.company)
print(vinshul.company)
print(tina.salary)  #priority given to instance attribute
print(vinshul.salary)

# class Programer:
#     companyee="Microsoft"
#     salary=10000
#     timeing="9am to 8pm"
#     depatment="software development"

# vinshul=Programer()
# print(vinshul.companyee)
# print(vinshul.salary)
# print(vinshul.timeing)
# print(vinshul.depatment)

