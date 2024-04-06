# Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no
def bisiesto_o_no(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
      return True
  return False

year =int(input("Por favor, introduzca el año: "))
if bisiesto_o_no(year):
    print(f"El año {year} es bisiesto.")
else:
    print(f"El año {year} no es bisiesto.")