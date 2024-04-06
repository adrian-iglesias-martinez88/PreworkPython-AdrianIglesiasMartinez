# Crea un programa que sume todos los números en una lista ingresada por el usuario.
def sumar_todo(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

numeros = list(map(int, input("Por favor, introduzca una lista de numeros separados por espacios: ").split()))
total = sumar_todo(numeros)
print(f"La suma de todos los numeros de la lista es de: {total}")