a=int(input("enter total marks of paper 1 :-  "))
b=int(input("enter total marks of paper 2 :-  "))
c=int(input("enter total marks of paper 3 :-  "))
 
p=int(input("/nenter marks of student in paper 1 :-  "))
q=int(input("enter marks of student in paper 2 :-  "))
r=int(input("enter marks of student in paper 3 :-  "))

per1=(100*p)/a
per2=(100*q)/b
per3=(100*r)/c

per=(per1+per2+per3)/3

if(per1>=33 and per2>=33 and per3>=33):
    if(per>=40):
        print("pass")
    else:
        print("fail due to you not having total percent grater than 40%")
else:
    print("fail due to having less than 33% in one of the subject")

if(per>=90):
    print("grade is Ex")
elif(per>=80):
    print("grade is A")
elif(per>=70):
    print("grade is B")
elif(per>=60):
    print("grade is C")
elif(per>=50):
    print("grade is D")
else:
    print("grade is F")
