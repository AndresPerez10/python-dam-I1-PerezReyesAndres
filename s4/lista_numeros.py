# Pedir números separados por comas
texto = input("Introduce números separados por comas: ")

# Separar y convertir a float (control de errores)
numeros = []
for x in texto.split(","):
    x = x.strip()
    try:
        numeros.append(float(x))
    except:
        print(f"'{x}' no es un número y se ignora.")

# Si hay números válidos, calcular resultados
if numeros:
    suma = sum(numeros)
    media = suma / len(numeros)
    mayor = max(numeros)
    duplicados = set([n for n in numeros if numeros.count(n) > 1])

    print("\nResultados:")
    print("Suma:", suma)
    print("Media:", media)
    print("Mayor:", mayor)
    print("Duplicados:", duplicados if duplicados else "No hay duplicados")
else:
    print("No se introdujeron números válidos.")
