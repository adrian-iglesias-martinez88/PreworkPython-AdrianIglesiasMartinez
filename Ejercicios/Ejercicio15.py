# Escribe un programa que convierta un número de minutos en horas y minutos. Por ejemplo, 145 minutos serían 2 horas y 25 minutos
def conversion_horas_minutos(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

minutos = int(input("Introduce el numero de minutos: "))
horas, minutos_restantes = conversion_horas_minutos(minutos)

print(f"{minutos} minutos seran en total {horas} horas y {minutos_restantes} minutos")