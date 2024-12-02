"""
p=""
l=[]
while (p!=":"):
    p = input("Introdueix una paraula ")
    if p!=":" and p[0]=="A":
        l.append(p)
print("Les paraules que comences per A son: {}".format(l))
print("ja hem acabat ")
"""

p=""
l=[]
while (p!="."):
     p = input("Introdueix una frase ")
     if p!=".":
         s= p.lower()
         p= s.title()
         l.append(p)
print("Les frases introduïdes son {}".format(l))
print("Ja hem acabt")

