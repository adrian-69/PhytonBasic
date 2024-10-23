def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Divisió per zero."

def mostrar_menu():
    print("\n--- Calculadora ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Sortir")

def calculadora():
    while True:
        mostrar_menu()
        op = input("Tria una operació (1/2/3/4/5): ")

        if op == '5':
            print("Sortint de la calculadora.")
            break

        if op in ['1', '2', '3', '4']:
            num1 = float(input("Introdueix el primer número: "))
            num2 = float(input("Introdueix el segon número: "))
            if op == '1':
                print(f"Resultat: {suma(num1, num2)}")
            elif op == '2':
                print(f"Resultat: {resta(num1, num2)}")
            elif op == '3':
                print(f"Resultat: {multiplicacio(num1, num2)}")
            elif op == '4':
                print(f"Resultat: {divisio(num1, num2)}")
        else:
            print("Operació no vàlida. Intenta-ho de nou.")

if __name__ == "__main__":
    calculadora()