# Escribe un programa que determine si un número ingresado por el usuario es primo o no.
def primo(numero):
    if numero <=1:
        return False
    for z in range(2, numero):
        if numero % 1 == 0:
            return False
    return True

numero = int(input("Introduce un numero: "))

if primo(numero):
      print(f"El numero {numero} es primo.")
else:
      print(f"El numero {numero} no es primo.")