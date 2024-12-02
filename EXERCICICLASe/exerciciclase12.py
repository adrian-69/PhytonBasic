"""#parametres 
#string/cadena de caracters ?? es passa per valor o per referencia 
def modifica_string(s):
    s="aixo es un canvi, anem a veure si fora de la funcio canvia o no "

s="Bon dia, aixo es una prova"
# per valor,la varianle c nos es modifica encara que jo no la modifiqui dins la funcio 
def operacio(a, b, c):
    c = a + b
a = 3
b = 4
c = 0
print(c)
operacio(a, b, c)
print(c)"""

def suma_llista(llista):
    suma = sum(llista)
    print("La suma dels elements de la llista és: {}")
   
   #Fem una nova llista 
    nova_llista = [e * 10 for e in llista]
    print("Elements de la llista multiplicats per 10:")
    for e in nova_llista:
        print(e)
    return nova_llista

#fem la suma de las dos llistes 
llista_original = [1, 2, 3, 4, 5]
nova_llista = suma_llista(llista_original)

print("Llista original:", llista_original)
print("Nova llista multiplicada per 10:", nova_llista)


