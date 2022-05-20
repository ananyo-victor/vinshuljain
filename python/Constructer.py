# class Employee:
#     compony="google"
#     def __init__(self):    #__init__(self)=constructor
#         print("employee is created")

# data=Employee()

#parameteraise constructor
class Employee:
    compony="google"
    def __init__(self,name,department,salary):    
        print("employee is created")
        print("welcome",name)
        print("Your depatment is",department)
        print("and your salary is",salary)
    def __init__(self):
        print("welcome to our site")

data=Employee("vinshul","computer",1000000)
# data=Employee()  #it through an error because there are four parameter and it contain only one
# Note:-constructor overloding is not possible .at one time it can access only one constructor 

# if there are two default constructor 
# class Employee:
#     compony="google"
    
#     def __init__(self):
#         print("welcome to our site")
#     def __init__(self):   #it will overwrite the data    
#         print("employee is created")
# data=Employee() #sacond constructor will printed