# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
def calculo_imc(peso, altura):
    imc = peso / (altura **2)
    return imc

peso = float(input("Introduce el peso en Kg: "))
altura = float(input("Introduce la altura en Metros: "))

imc = calculo_imc(peso, altura)
print(f"El IMC es: {imc:.2f}")