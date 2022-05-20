#what is strip unction
a="     vinshul is a coder        "
# print(a)
# print(a.strip())

#string remover

def f1(string,word):
    new=string.replace(word,"")
    return new.strip()

n=f1(a,"vinshul")
print(n)