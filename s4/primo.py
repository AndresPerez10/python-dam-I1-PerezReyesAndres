# Programa que dice si un número es primo o no

import time

try:
    n = int(input("Introduce un número: "))

    print("\n🔍 Comprobando si el número es primo...\n")
    
    # Comprobación de número primo
    if n < 2:
        es_primo = False
    else:
        es_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break

    # Mostrar resultado
    if es_primo:
        print(f"\n✅ {n} es un número primo")
    else:
        print(f"\n❌ {n} no es primo")

    # Extra personal: decir si es par o impar
    if n % 2 == 0:
        print("Además, es un número PAR ⚙️")
    else:
        print("Además, es un número IMPAR ⚡")

except ValueError:
    print("Error: introduce un número válido.")
