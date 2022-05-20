a=int(input("enter the no. 1:-  "))
b=int(input("enter the no. 2:-  "))
c=int(input("enter the no. 3:-  "))
# d=int(input("enter the no. 4:-  "))
# if(a>b and a>c and a>d):
#     print(a ," is gatest")
# elif(b>c and b>d):
#     print(b ," is gratest")
# elif(c>d):
#     print(c,"is gratest")
# else:
#     print(d, " is gratest")

# or

# if(a>b):
#     f1=a
# else:
#     f1=b
# if(c>d):
#     f2=c
# else:
#     f2=d
# if(f1>f2):
#     print(str(f1) + " is gratest")
# else:
#     print(f2,"is gtatest")

# using a funtion and finding gratest among 3 no.
def gratest(p,q,r):
    if(p>q and p>r):
        print(p, "is gratest")
    elif(q>r):
        print(q,"is gratest")
    else:
        print(r,"is gratest")

gratest(a,b,c)