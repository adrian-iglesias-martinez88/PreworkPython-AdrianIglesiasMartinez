# Crea un programa que verifique si una palabra ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def palindromo(palabra):
    palabra_invertida = palabra [::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

palabra = input("Introduzca la palabra que usted quiera: ")

if palindromo(palabra):
    print("Es un palindromo")
else:
    print("No es un palindromo")