# Cuenta vocales, consonantes, mayúsculas y caracteres totales

import time

texto = input("Escribe una frase: ")

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
num_vocales = 0
num_consonantes = 0
num_mayus = 0

# Contar letras
for c in texto:
    if c.isalpha():
        if c in vocales:
            num_vocales += 1
        else:
            num_consonantes += 1
    if c.isupper():
        num_mayus += 1

# Total de caracteres
num_total = len(texto)


print("\n🔍 Analizando tu texto...\n")
time.sleep(0.5)
print("🟩 Vocales:", num_vocales)
time.sleep(0.3)
print("🟦 Consonantes:", num_consonantes)
time.sleep(0.3)
print("🔠 Mayúsculas:", num_mayus)
time.sleep(0.3)
print("📏 Total de caracteres:", num_total)

# Extra Personal
print("\n🎨 Visualización:")
print("Vocales:      " + "🟩" * num_vocales)
print("Consonantes:  " + "🟦" * num_consonantes)
print("Mayúsculas:   " + "🟥" * num_mayus)

if num_mayus == 0:
    print("\n😴 Energía baja... ¡Agrega MAYÚSCULAS para más poder!")
elif num_mayus < 5:
    print("\n⚡ Energía moderada. ¡Buen equilibrio!")
else:
    print("\n🔥 ¡Texto poderoso! ¡LLENO DE ENERGÍA!")
