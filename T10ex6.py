def longitud(element):
    """Calcula la longitud d'una llista o d'una cadena."""
    return len(element)

# Proves amb diferents exemples
# Proves amb cadenes
cadena1 = "Hola, món!"
cadena2 = "Python"

print("Longitud de la cadena '{}': {}".format(cadena1, longitud(cadena1)))  # Ha de retornar 12
print("Longitud de la cadena '{}': {}".format(cadena2, longitud(cadena2)))  # Ha de retornar 6

# Proves amb llistes
llista1 = [1, 2, 3, 4, 5]
llista2 = ['a', 'b', 'c']

print("Longitud de la llista {}: {}".format(llista1, longitud(llista1)))  # Ha de retornar 5
print("Longitud de la llista {}: {}".format(llista2, longitud(llista2)))  # Ha de retornar 3

