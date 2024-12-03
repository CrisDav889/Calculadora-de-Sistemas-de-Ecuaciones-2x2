import calculo as c
print("Bienvenido a la calculadora 2 x 2: ")
while True:
    x, y, z = c.leer_ecua()
    compro = input("ingreso correctamente los datos? (Si/No)")
    if compro.lower() == 'no':
        continue
    else:
        c.ecuacion(x, y, z)
