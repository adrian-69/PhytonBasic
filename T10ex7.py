def es_vocal(caracter):
    return caracter.lower() in 'aeiou'

# Proves amb diferents exemples
print(es_vocal('a'))  # Verdader
print(es_vocal('E'))  # Verdader
print(es_vocal('t'))  # Fals
print(es_vocal('u'))  # Verdader
print(es_vocal('x'))  # Fals