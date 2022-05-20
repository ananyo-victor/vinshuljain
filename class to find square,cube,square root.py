# class formula:
#     def square(self):
#         return self.a*self.a 
#     def cube(self):
#         return self.a*self.a*self.a 
#     def squareroot(self):
#         b=20
#         h=1
#         while b>10:
#             if int(h*h)==self.a:
#                 return h
#             elif int(h*h)>self.a:
#                 return "square root is not possible"
#             else:
#                 h=h+1

# num=formula()
# num.a=10
# n1=num.square()
# n2=num.cube()
# n3=num.squareroot()
# print(n1)
# print(n2)
# print(n3)

'''Or'''

class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"the square of {self.number} is {self.number**2}")
    def cube(self):
        print(f"the cube of {self.number} is {self.number**3}")
    def squareroot(self):
        print(f"the square root of {self.number} is {self.number**0.5}")
    @staticmethod
    def gread():
        print("wlecome to the world of best calculator")

object=Calculator(11)
object.gread()
object.square()
object.cube()
object.squareroot()