# Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.
def calcular_edad(year_nacimiento):
    year_actual = 2024
    edad = year_actual - year_nacimiento
    return edad

year_nacimiento = int(input("Introduce el año en el que has nacido: "))
edad = calcular_edad(year_nacimiento)

print(f"Tu edad es {edad} años")