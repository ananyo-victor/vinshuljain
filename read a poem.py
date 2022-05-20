with open("poem.txt","w") as f:
    data=f.write('''Twinkle, Twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')
with open("poem.txt","r") as f:
    data=f.read()
    if "Twinkle" in data:
        print("Yes it is present")
    else:
        print("No it is not present")
# print(data)
