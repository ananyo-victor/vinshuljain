class Complex_no:
    def __init__(self,a,b):
        self.real=a
        self.imaginary=b

    def __add__(self,c):
        print([self.real+c.real],str([self.imaginary+c.imaginary])+"i")
    
    def __mul__(self,c):
        print([self.real*c.real-(self.imaginary*c.imaginary)],str([self.real*c.imaginary+(self.imaginary*c.real)])+"i")

c1=Complex_no(1,2)
c2=Complex_no(3,4)
sum=c1+c2
mul=c1*c2
print(sum)
print(mul)