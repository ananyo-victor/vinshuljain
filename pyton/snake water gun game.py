# randum module


upoint=0
cpoint=0
for i in range(10):
    import random   #random is a module
    print("comp turn: snake(s) water(w) or gun(g)?")
    randno = random.randint(1,3)  # it print random no. between 1,2,3
    if randno==1:
        comp="s"
    elif randno==2:
        comp="w"
    elif randno==3:
        comp="g"

    user=input("your turn: snack(s) water(w) or gun(g) ?")
    def game(a,b):
        if a=='s' and b=='g':
            print("user win's")
            return '1'
            # upoint=int(upoint)+1   # it will not work
        elif a=='w' and b=='s':
            print("user win's")
            
            return '1'
        elif a=='g' and b=='w':
            print("user win's")
            return '1'
        elif a==b:
            print("tie")
            return '2'
        else:
            print("comp win's")
            return '0'
    print(comp)
    g=int(game(comp,user))
    # print(g)
    if g==1:
        upoint=upoint+1
    if g==0:
        cpoint=cpoint+1

    print("\nuser points are",upoint)
    print("comp point are",cpoint)
if(cpoint>upoint):
    print("computer wis's the match")
elif(upoint>cpoint):
    print("user win's the match")
else:
    print("match draw's")