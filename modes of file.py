'''
r=reading #it is done in file 
w=writing
a=appending
+=updating
'''

'''
note:- for binary mode we write 'rb' ,'wb','ab','+b' 
:- in case of text mode it by default print t at the end of r and so no...
'''

# # writing a file
# f=open("another.txt","w")  # if there is no file of that name than it atomatically create a file
# f.write("please write this to the file\n")
# f.write("please write this to the file2\n")
# f.close()

# # appending a file
# f=open("another.txt","a")  # if there is no file of that name than it atomatically create a file
# f.write("i am appending")
# f.close()

# with statement
# with open("another.txt","w") as f:  #while using the with we should not have to close the the file it atomatically close it 
#     a=f.write("i am writing")
# with open("another.txt","r") as f:
#     a=f.read()
# print(a)

#updating
# words=["moti","donkey","good"]
# with open("sample.txt","r") as f:
#     r=f.read()
# for i in words:
#     r=r.replace(i,"######")

#     with open("sample.txt","w") as f:
#         f.write(r)

#python is present in log file or not
# with open("log.txt","r") as f:
#     log=f.readline().lower()  # it will lower every case
# g=log.find("python")
# if g>0:
#     print("it contain python")
# else:
#     print("no python is not present")

# python is present in which line
# log=True
# i=1
# with open("log.txt","r") as f:
#     while log:
#         log=f.readline()  
#         if "python" in log.lower():
#             print("it contain python")
#             print(i)
#         i=i+1

# copy a File
# with open("sample.txt") as f:
#     copy=f.read()
# with open("copy.txt",'w') as f:
#     f.write(copy)

# file is identical or have maching contain 
with open("sample.txt") as f1:
    s=f1.read()
with open("copy.txt") as f2:
    b=f2.read()

if s==b:
    print("it is identical")
else:
    print("it is not identical")
