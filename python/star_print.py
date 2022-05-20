# j=3
# for i in range(7):
#     if i%2==0:
#         continue
#     print(" " * int(5-j),  "*" * i )
#     j=j+1

'''OR'''

# n=3
# for i in range(3):
#     print(" " * (n-1-i),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))


# for i in range(3):
#     print("*" * (i+1))
    
# a=3
# for i in range(a):
#     if(i==0 or i==(a-1)):
#      print("* " * a)
#     else:
#         print("*"+ " "*(2*a-3)+"*")
    
def star():
    n=3
    for i in range(n):
        print("* " * (n-i))
print(star())