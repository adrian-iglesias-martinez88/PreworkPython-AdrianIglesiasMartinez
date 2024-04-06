# Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la longitud y el ancho del rectángulo
def cal_area_rec(longitud, ancho):
    area = longitud * ancho
    return area

longitud = float(input("Introduce la longitud: "))
ancho = float(input("Introduce el ancho: "))

calcular_area = cal_area_rec(longitud, ancho)
print(f"El area del rectangulo es: {calcular_area}")