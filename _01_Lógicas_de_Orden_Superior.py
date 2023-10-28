def aplicar_funcion(func, x):
    return func(x)

# Definir una funci�n simple
def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

# Aplicar la funci�n cuadrado a un valor
resultado = aplicar_funcion(cuadrado, 5)
print("Cuadrado de 5:", resultado)

# Aplicar la funci�n cubo a un valor
resultado = aplicar_funcion(cubo, 3)
print("Cubo de 3:", resultado)

# Funci�n que devuelve una funci�n
def seleccionar_funcion(potencia):
    if potencia == 2:
        return cuadrado
    elif potencia == 3:
        return cubo

# Obtener una funci�n en funci�n de un valor
func = seleccionar_funcion(2)
resultado = aplicar_funcion(func, 4)
print("Cuadrado de 4:", resultado)

func = seleccionar_funcion(3)
resultado = aplicar_funcion(func, 2)
print("Cubo de 2:", resultado)
