# Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.
def calcular_precio_final(precio):
    descuento = precio * 0.2
    total = precio - descuento
    return total

precio_base = float(input("Introduzca el precio del articulo: ")) 
precio_con_descuento = calcular_precio_final(precio_base)

print(f"El precio del articulo con el descuento es de: {precio_con_descuento} Euros")