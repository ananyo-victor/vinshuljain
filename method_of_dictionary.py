mydic={
    "fast":"In a Quick manner",
    "vinshul":"a coder",
    "marks":[1,2,4],
    "anotherdict":{'vinshul':'player'},#nested dictionary
    1 : 2
}
print (mydic.keys())#print dic key
print(type(mydic.keys()))
print(list(mydic.keys()))#convert dic into list
print(mydic.values())#print value of key
print(mydic.items())#print all(key,value) of dic
updatedict={
    'ram':'friend',
    'ananyo':'friend',
    'kapil':'frind'
}
mydic.update(updatedict)#add new key,value in dic
print(mydic)
print(mydic.get("vinshul"))
print(mydic["vinshul"])
# print(mydic["vinshul2"])#through error
print(mydic.get("vinshul2"))
