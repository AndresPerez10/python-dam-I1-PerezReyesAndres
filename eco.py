# Programa en Python que pide 3 números y muestra:
# - La suma de los números
# - La media (promedio)
# - El número mayor

# Pedir tres números al usuario y convertirlos a float (para aceptar decimales)
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
n3 = float(input("Introduce el tercer número: "))

# Calcular la suma
suma = n1 + n2 + n3

# Calcular la media (promedio)
media = suma / 3

# Encontrar el número mayor con la función max()
mayor = max(n1, n2, n3)

# Mostrar resultados
print("\nResultados:")
print(f"Suma = {suma}")
print(f"Media = {media}")
print(f"Mayor = {mayor}")
