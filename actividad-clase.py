# Pedir al usuario un número
n = int(input("Introduce un número: "))

# Recorrer del 1 hasta n
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} -> {i ** 2}")
    else:
        print(i)
