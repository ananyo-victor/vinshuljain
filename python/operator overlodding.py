class Calculator:
    def __init__(self,num):
        self.num=num

    def __add__(self, num2):  #__add__ :-called (dunder add)
        print("let's add")
        return self.num + num2.num  #now it print the correct ans
        # return 300   #print ans 300
    
    def __mul__(self,num2):
        print("let's multiply")
        return self.num * num2.num
    
    def __sub__(self,num2):
        print("let's subtract")
        return self.num - num2.num

    def __truediv__(self,num2):
        print("let's devide")
        return self.num / num2.num

    def __floordiv__(self,num2):
        print("let's find reminder")
        return self.num % num2.num

    #some more method
    def __str__(self):
        return f"the decimal no. is {self.num}"

    def __len__(self):
        return 1
n1=Calculator(3)
n2=Calculator(6)
print(n1)
print(len(n1))
sum=n1+n2
mul=n1*n2
sub=n2-n1
div=n2/n1
rem=n2//n1
print(sum)
print(mul)
print(sub)
print(div)
print(rem)

'''note:- for more oprator to overlood,search on google(python doc for operator overlodding)'''

class vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1=vector([7,8,10])
print(v1)