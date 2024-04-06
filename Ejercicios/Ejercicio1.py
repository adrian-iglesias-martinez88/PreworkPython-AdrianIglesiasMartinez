# Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
def cel_far(celsius):
    return celsius * (9/5) + 32

temp_cel = float(input("Introduce la temperatura en grados Celsius: "))
temp_far = cel_far(temp_cel)
print(f"La temperatura en grados Farenheit es: {temp_far}")