# Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.
def palabras_conteo(oracion):
    palabras = oracion.split()
    numero_palabras = len(palabras)
    return numero_palabras

frase = input("Por favor, introduce una frase completa con su sujeto, verbo y predicado: ")
total_palabras = palabras_conteo(frase)
print(f"La frase contiene un total de {total_palabras} palabras.")