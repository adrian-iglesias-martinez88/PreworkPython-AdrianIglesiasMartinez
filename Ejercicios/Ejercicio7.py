# Crea un programa que realice operaciones aritméticas simples (suma, resta, multiplicación, división) según la elección del usuario.
numero1=float(input("Introduce el primer numero:"))
numero2=float(input("Introduce el segundo numero:"))

numero = 0

while numero != 5:
    print("""
    Indique la operacion que desea realizar
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir
    """)

    numero = float (input())

    if numero == 1:
        print(" ")
        print("Resultado: ", numero1,"+", numero2,"=",numero1+numero2)
    if numero == 2:
        print(" ")
        print("Resultado: ", numero1,"-", numero2,"=",numero1-numero2)
    if numero == 3:
        print(" ")
        print("Resultado: ", numero1,"*", numero2,"=",numero1*numero2)
    if numero == 4:
        print(" ")
        print("Resultado: ", numero1,"/", numero2,"=",numero1/numero2)
    if numero == 5:
        print("Gracias por usar la calculadora de Adrian Iglesias Martinez")