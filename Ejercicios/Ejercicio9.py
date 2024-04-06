# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
def dol_eur(dolares):
    euros = dolares + 0.85
    return euros

cant_dol = float(input("Introduce la cantidad en dolares: "))
cant_eur = dol_eur(cant_dol)

print(f"La cantidad en euros es: {cant_eur}")