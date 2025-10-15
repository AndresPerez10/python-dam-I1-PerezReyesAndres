# Conversor de grados Celsius a Kelvin

# Pedir al usuario la temperatura en grados Celsius
try:
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    
    # Convertir a Kelvin
    kelvin = celsius + 273.15

    # Mostrar resultado
    print(f"\n{celsius} °C equivalen a {kelvin} K")

    # Añadido presonal: clasificar la temperatura
    if celsius < 0:
        print("Hace mucho frío ❄️")
    elif celsius < 25:
        print("Temperatura templada 🌤️")
    else:
        print("Hace calor ☀️")

except ValueError:
    print("Error: introduce un número válido.")
