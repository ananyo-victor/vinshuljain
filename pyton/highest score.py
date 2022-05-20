
def game():
    return 23
score=int(game())
with open("hiscore.txt","r") as g:
    hiscore=g.read()
if  hiscore=="":
    with open("hiscore.txt","w") as g:
        g.write(str(score))
elif int(hiscore)<score:
    with open("hiscore.txt","w") as g:
        g.write(str(score))
with open("hiscore.txt","r") as g:
    hiscore=int(g.read())
    print(hiscore)

