import numpy as np

def producto_punto(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.dot(v1, v2)

# Ejemplo 
v1 = [2, -1, 3]
v2 = [1, 4, 0]

resultado = producto_punto(v1, v2)
print("El producto punto es:", resultado)
