def leer_ecua():
    x = []
    y = []
    z = []
    ecua = [x, y, z]
    letras = ["x", "y", "z"]
    for i in range(0, len(ecua)):
        letra = letras[i]
        for j in range(0, 2):
            ecua[i].append(float(input(f"ingrese el valor en la ecuacion 1: {letra} en l"
                                       f"ecuacion {j + 1}: ")))
    return x, y, z


def ecuacion(x, y, z):
    d = determinante(x, y)
    dx = det_x(y, z)
    dy = det_y(x, z)
    valor_x = dx / d
    valor_y = dy / d
    print(f"El valor de x es: {valor_x}")
    print(f"El valor de y es: {valor_y}")
    # Determinante en x & y


def determinante(x, y):
    d = x[0] * y[1] - x[1] * y[0]
    return d


def det_x(y, z):
    dx = z[0] * y[1] - z[1] * y[0]
    return dx


def det_y(x, z):
    dy = x[0] * z[1] - x[1] * z[0]
    return dy
