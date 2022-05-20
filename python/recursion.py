# example of factorial
# n=4
# product=1
# for i in range(n):
#     product=product*(i+1)
# print(product)

# def factorial_iter(n):
#     product=1
#     for i in range(n):
#         product=product*(i+1)
#     return product

def factorial_recurtion(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recurtion(n-1)

''' Working of factorial 
    factorial(4)=4*factorial(3)
    factorial(3)=3*factorial(2)
    factorial(2)=2*factorial(1)
    if n==1
    factorial(1)=1
    hence,factorial(4)=4*3*2*1
'''
f=factorial_recurtion(3)
print(f)
