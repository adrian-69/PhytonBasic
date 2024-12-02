a= int(input("Escriu un numero: "))
b= int(input("Escriu un numero: "))
c= int(input("Escriu un numero: "))
if a > b:
    if b > c:
        print("{} es major que {} i aquest es major que {}".format(a, b, c))
    elif b<c:
        if a<c:
            print("{} es major que {} i aquest es major que {}".format(a, c, b))
    elif c>a:
        print("{} es major que {} i aquest es major que {}".format(c, a, b ))
    else:
        print("{} i {} i son iguals o major{}".format(c, a, b ))