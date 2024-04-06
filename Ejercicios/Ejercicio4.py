# Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
def count_vocales(palabra):
    vocal = "AEIOUaeiou"
    contador = 0
    for letra in palabra:
        if letra in vocal:
            contador +=1
    return contador

palabra = input("Introduzca la palabra o frase: ")
numero_de_vocales = count_vocales(palabra)

print(f"El total de vocales de la palabra o frase es: {numero_de_vocales}")