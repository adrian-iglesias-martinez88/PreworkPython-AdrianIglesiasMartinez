# Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
def det_dia(numero):
    dia_semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    if numero >= 1 and numero <= 7:
        return dia_semana[numero-1]
    
numero = int(input("Indique un numero del 1 al 7: "))
nombre_dia = det_dia(numero)
print(f"El dia correspondiente es el: {nombre_dia}")