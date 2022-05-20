a={1,2,9,6,'a',5,7,(1,2,1)}
print(len(a))#print length of set a
print(a)
'''note:- it show the output in assending order '''
a.remove(2)
# a.remove(15)#show error to remove 15 because it is not present in set
print(a)

a.add(3)#addding a element
print(a)

a.pop()#delete the first element of assending order
print(a)

print(a.union({8,13,11}))#print union
print(a.union({1,9}))

print(a.intersection({1,9}))#print intersection
print(a.intersection({11,12}))#no element match emety set will be printed

a.clear()#clear whole set
print(a)