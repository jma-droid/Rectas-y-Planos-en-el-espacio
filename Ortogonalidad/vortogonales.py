import numpy as np

def son_ortogonales(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    # Producto punto con NumPy
    producto_punto = np.dot(v1, v2)

    return producto_punto == 0

# Ejemplo de vectores ortogonales en R3
v1 = [0, -1, 2]
v2 = [1, 2, 1]

if son_ortogonales(v1, v2):
    print("Los vectores son ortogonales.")
else:
    print("Los vectores no son ortogonales.")

