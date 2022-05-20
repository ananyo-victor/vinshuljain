class Train:
    def book_a_ticket(self,name,to,dastiny,trainName):
        print("you name is",name)
        print("going from",to)
        print("dastiny to reach",dastiny)
        print("name of train",trainName,)
    def get_status(self,setno,trainName):
        print(f"your {setno} sit are in {trainName}")
    def information(self):
        print("at platform no. 1:- shanti express")
        print("at platform no. 2:- gujarat express")
        print("at platform no. 3:- kanpur express")
        print("at platform no. 4:- indore express")
k=1
while k>0:
    object=Train()
    print("\nwelcome to railway department\nyou can perform following feture\n1.Booking of ticket\n2.Get status of train\n3.Information of your train")
    a=int(input())
    if a==1:
        p1=input("enter your name:- ")
        p2=input("enter from where you are going:- ")
        p3=input("enter your dastiny:- ")
        p4=input("enter train name:- ")
        object.book_a_ticket(p1,p2,p3,p4)
    elif a==2:
        s=input("enter no. of set")
        object.get_status(s,p4)
    elif a==3:
        object.information()
    else:
        print("invalid choice")
