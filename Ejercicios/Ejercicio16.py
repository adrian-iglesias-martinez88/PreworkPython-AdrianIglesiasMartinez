# Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.
def conteo_par_impar(listado):
    pares = 0
    impares = 0
    for num in listado:
        if num % 2 == 0:
            pares = pares + 1
        else:
            impares += 1
    return pares, impares

numeros = list(map(int, input("Por favor, introduce una lista de numeros separados por espacios: ").split()))
pares, impares = conteo_par_impar(numeros)
print(f"La lista se compone de {pares} numeros pares y {impares} numeros impares.")