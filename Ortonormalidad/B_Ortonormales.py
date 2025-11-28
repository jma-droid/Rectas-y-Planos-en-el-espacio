import numpy as np
def es_ortogonal(base, tol=1e-8):
    
    #Verifica si un conjunto de vectores es ortogonal.
    #base: matriz donde cada fila es un vector.
    
    n = base.shape[0]

    for i in range(n):
        for j in range(i+1, n):
            producto = np.dot(base[i], base[j])
            if abs(producto) > tol:
                return False
    return True

def es_ortonormal(base, tol=1e-8):
    
    #Verifica si una base es ortonormal:
    #- Los vectores son ortogonales
    #- Cada vector tiene norma 1
    
    if not es_ortogonal(base, tol):
        return False
    
    # Comprobar norma unitaria
    for vec in base:
        if abs(np.linalg.norm(vec) - 1) > tol:
            return False
    return True

# EJEMPLO 1: base ortonormal
A = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# EJEMPLO 2: base no ortonormal
B = np.array([
    [1, 1],
    [1, 0]
])

# Mostrar resultados
print("BASE A")
print("Ortogonal:", es_ortogonal(A))
print("Ortonormal:", es_ortonormal(A))

print("\nBASE B")
print("Ortogonal:", es_ortogonal(B))
print("Ortonormal:", es_ortonormal(B))
