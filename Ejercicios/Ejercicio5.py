# Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
sum = 0
for num in range (2, 101, 2):
    sum += num

print(f"La suma total de los numeros pares es: {sum}")