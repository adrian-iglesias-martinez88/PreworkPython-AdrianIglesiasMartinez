# Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.
def su_edad(edad):
    if edad > 17:
        return "Usted es mayor de edad"
    else:
        return "Usted es mmenor de edad"

edad = int(input("Introduzca su edad: "))
comprobar = su_edad(edad)
print(comprobar)