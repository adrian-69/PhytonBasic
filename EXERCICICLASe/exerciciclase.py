"""
l=[4,6,8,10]
r = list(map(lambda x:x *2,l))
print(r)
"""
n= int(input("Introdueix un numero a fer el factorila: "))
r=1
while(n>0):
    r=r*n
    n=n-1
print(r)

#fer el factorial en recursivitat
def fact(n):
    if n<=0:
        return 1
    else:
        return n * fact(n-1)
print(fact(3))
