import numpy as np

def proyeccion(u, v):
    u = np.array(u, dtype=float)
    v = np.array(v, dtype=float)

    # Fórmula de la proyección: proj_v(u) = ( (u·v) / (v·v) ) * v
    escalar = np.dot(u, v) / np.dot(v, v)
    proy = escalar * v
    return proy

# Vectores del ejemplo
u = [2, -1, 3]
v = [1, 4, 2]

proy = proyeccion(u, v)
print("La proyección de u sobre v es:", proy)
