list=[97,87,77,54,32,31,11,9]
for n in range(7):
    def sort():
        if list[n]>=list[n+1]:
            return "true"
        else:
            return "false"
    if(sort()=="false"):
        break

s=sort()
if s=="false":
    print("list is unsorted")
else:
    print("list is sorted")
