mydic={
    "fast":"In a Quick manner",
    "vinshul":"a coder",
    "marks":[1,2,4],
    "anotherdict":{'vinshul':'player'},#nested dictionary
    1:2
}
print(mydic['fast'])
print(mydic["vinshul"])
print(mydic['''marks'''])
print(mydic[1])
print(mydic['anotherdict']["vinshul"])
mydic['marks']=[45,67]#changes permanently
print(mydic['marks'])
print(mydic)
# note :- we cannot use diplicate key in dic 