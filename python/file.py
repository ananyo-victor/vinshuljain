#use open function to read the content of a file

f=open("file.txt",'r') #open is a in built function
# f=open('sample.txt')# by default it read the file
# data=f.read()   #read is also a in built funtion
# data=f.read(5) # it will read first five character
# print(data)
# f.close()#remamber we should always close the file

#other function to read the file
print(f.tell())#tell the position of file pointer
data=f.readline() #read first  line
print(data) 
print(f.tell())
data=f.readline() #read second line
print(data)
data=f.readline() #so on....
f.seek(0)  #it will reset line
print(data)
data=f.readline()
print(data)
data=f.readline()
print(data)
