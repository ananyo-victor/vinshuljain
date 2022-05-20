# n=int(input("enter the no. :- "))
# i=1
# j=0
# while(i<=n):
#     j=j+i
#     i=i+1
# print(j)

# sum of natural no. using recuricive method
def sum(n):
    if n==1:
        return 1
    return (n+sum(n-1))

num=sum(5)
print(num)
