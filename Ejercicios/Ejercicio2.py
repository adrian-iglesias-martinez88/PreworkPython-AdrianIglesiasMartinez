# Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta.
def calculo_total(consumo):
    propina = consumo * 0.15
    total= consumo + propina
    return total

consumo = float(input("Introducir el total de la cuenta: "))
total_cuenta = calculo_total(consumo)
print(f"El total de la cuenta incluida la propia es de: {total_cuenta}")