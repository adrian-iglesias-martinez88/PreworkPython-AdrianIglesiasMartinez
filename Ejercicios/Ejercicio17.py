# Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.
def transformar_millas_km(millas):
    km = millas * 1.60
    return km

millas = float(input("Por favor, introduce la distancia en millas: "))
km = transformar_millas_km(millas)
print(f"La distancia total en kilometros es: {km} ")