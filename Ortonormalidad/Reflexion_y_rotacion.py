import numpy as np

#Vector original
v = np.array([3, 2])   # Puedes cambiarse

# Reflexión respecto al eje x
R_x = np.array([
    [1, 0],
    [0, -1]
])

# Rotación de 90 grados (π/2 radianes)
theta = np.pi / 2
T = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

#Operaciones / Formulas
v_reflejado = R_x @ v
v_rotado = T @ v

#Resultados
print("Vector original:", v)
print("\n Reflexión respecto al eje x")
print("Matriz de reflexión:\n", R_x)
print("Resultado:", v_reflejado)

print("\n Rotación 90° (π/2 rad)")
print("Matriz de rotación:\n", T)
print("Resultado:", v_rotado)
