import random
randomno=random.randint(1,50)
i=0
while i<1:
    user=int(input("enter a no.  :- "))
    if(user>50):
        print("Guessed no. is out of range")
    elif(user<1):
        print("Guessed no. is out of range")
    elif(user<randomno):
        print("Higher no. please")
    elif(user>randomno):
        print("Lower no. please")
    elif(randomno==user):
        break

print("Hurry! You won")