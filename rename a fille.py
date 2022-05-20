import os
with open("sample2.txt") as f:
    rename=f.read()
with open("rename.txt",'w') as f:
    f.write(rename)
os.remove("sample2.txt")