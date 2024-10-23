def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacio(x, y):
    return x * y

def divisio(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Divisió per zero!"

def canvi_base(num, base):
    if base == 'bin':
        return bin(num)
    elif base == 'oct':
        return oct(num)
    elif base == 'hex':
        return hex(num)
    else:
        return "Error: Base no reconeguda!"

def calculadora():
    print("Opcions:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Canvi de base")
    
    opcio = input("Tria una opció (1-5): ")

    if opcio in ['1', '2', '3', '4']:
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))

        if opcio == '1':
            print("Resultat:", suma(num1, num2))
        elif opcio == '2':
            print("Resultat:", resta(num1, num2))
        elif opcio == '3':
            print("Resultat:", multiplicacio(num1, num2))
        elif opcio == '4':
            print("Resultat:", divisio(num1, num2))

    elif opcio == '5':
        num = int(input("Introdueix un número decimal: "))
        base = input("Introdueix la base (bin, oct, hex): ")
        print("Resultat:", canvi_base(num, base))
    else:
        print("Opció no vàlida!")

def gran(num1, num2):
    return max(num1, num2)

def gran_de_tres(num1, num2, num3):
    return max(num1, num2, num3)

# Proves de les funcions gran() i gran_de_tres()
print("Proves de gran():")
print(gran(5, 10))  # Ha de retornar 10
print(gran(-1, -5))  # Ha de retornar -1
print(gran(15, 25))  # Ha de retornar 25

print("\nProves de gran_de_tres():")
print(gran_de_tres(5, 10, 3))  # Ha de retornar 10
print(gran_de_tres(-1, -5, -3))  # Ha de retornar -1
print(gran_de_tres(15, 25, 20))  # Ha de retornar 25
print(gran_de_tres(7, 7, 7))  # Ha de retornar 7

# Inicia la calculadora
calculadora()


