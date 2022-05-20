#use open function to read the content of a file

f=open('sample.txt','r') #open is a in built function
# f=open('sample.txt')# by default it read the file
# data=f.read()   #read is also a in built funtion
# data=f.read(5) # it will read first five character
# print(data)
# f.close()#remamber we should always close the file

#other function to read the file

data=f.readline() #read first  line
print(data) 
data=f.readline() #read second line
print(data)
data=f.readline() #so on....
print(data)
data=f.readline()
print(data)
data=f.readline()
print(data)
