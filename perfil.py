from datetime import datetime

# Pedir datos
nombre = input("Introduce tu nombre: ")

anio = input("Introduce tu año de nacimiento (YYYY): ")

# Verificar que el año sea número
if not anio.isdigit():
    print("Error: Debes introducir un número.")
else:
    anio = int(anio)
    edad = datetime.now().year - anio

    # Clasificación
    if edad < 18:
        tramo = "Menor de edad (<18)"
    elif edad <= 65:
        tramo = "Adulto (18-65)"
    else:
        tramo = "Adulto mayor (>65)"

    # Resultado
    print(f"\nHola {nombre}, tienes {edad} años.")
    print(f"Clasificación: {tramo}")