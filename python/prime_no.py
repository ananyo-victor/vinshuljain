a=int(input("enter the no. :- "))
i=2
j=0
while(i<a):
    if(a%i==0):
        j=1
    i=i+1

if j==1:
    print("no. is non-prime")
else:
    print("no. is prime")