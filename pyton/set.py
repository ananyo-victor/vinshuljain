# a={1,2,4,5,1}#in set no element can be repeted
# print(type(a))
# print(a)


#important : his syntax will create an empty dictionary and not an empty set
a={}
print(type(a))

#an empty set can be created using the below syntax :
b=set()
print(type(b))
#adding the value to empty set
b.add(4)
b.add(4)#it will print 4 one time only
b.add(5)
# b.add(3,4)#through error
b.add((6,1,2))
# b.add({4:5})#we can not add list or dictionry in set
print(b)

'''Note:-
-> set are un indexed(we cannot say print(a[1]))
-> there is noway to change iteam in set
-> set cannot have duplicate value 
'''