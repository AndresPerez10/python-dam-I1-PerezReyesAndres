# analisis_notas.py
# Programa que analiza una lista de calificaciones separadas por comas

# Pedir las notas
entrada = input("Introduce las notas separadas por comas: ")

# Convertir a lista de floats
# Separa, limpia y convierte a float solo los elementos válidos
notas = []
for x in entrada.split(","):
    x = x.strip()
    if x:  # si no está vacío
        try:
            notas.append(float(x))
        except ValueError:
            print(f"Error: '{x}' no es un número válido.")
            exit()

# Si no hay notas válidas
if not notas:
    print("No se introdujeron notas válidas.")
    exit()

# Calcular datos
total = len(notas)
media = sum(notas) / total
nota_min = min(notas)
nota_max = max(notas)

# Porcentajes
aprobados = len([n for n in notas if n >= 5]) * 100 / total
sobresalientes = len([n for n in notas if n >= 9]) * 100 / total

# Calcular moda (nota más repetida)
frecuencias = {}
for n in notas:
    frecuencias[n] = frecuencias.get(n, 0) + 1
max_frecuencia = max(frecuencias.values())
modas = [n for n, f in frecuencias.items() if f == max_frecuencia]

# Mostrar resultados
print("\n--- Resumen de notas ---")
print(f"Número total de notas: {total}")
print(f"Media: {media:.2f}")
print(f"Nota mínima: {nota_min}")
print(f"Nota máxima: {nota_max}")
print(f"Porcentaje de aprobados: {aprobados:.1f}%")
print(f"Porcentaje de sobresalientes: {sobresalientes:.1f}%")
print("Nota(s) más repetida(s):", ", ".join(map(str, modas)))

# Mensaje final
if media >= 8:
    print("Nivel excelente")
elif media >= 5:
    print("Nivel medio")
else:
    print("Necesita refuerzo")
