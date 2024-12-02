def sumar_llista(llista):
    return sum(llista)

def multiplicar_llista(llista):
    resultat = 1
    for numero in llista:
        resultat *= numero
    return resultat

# Proves amb diferents exemples
print(sumar_llista([1, 2, 3, 4]))  
print(sumar_llista([10, 20, 30]))   

print(multiplicar_llista([1, 2, 3, 4]))  
print(multiplicar_llista([2, 3, 4]))     
print(multiplicar_llista([0, 1, 2]))     