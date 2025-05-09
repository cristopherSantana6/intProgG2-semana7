
N = int(input("Ingresa un número entero positivo: "))


if N > 0:
    suma = 0  

    
    for i in range(1, N + 1):
        suma += i

    
    print(f"La suma de los números del 1 al {N} es: {suma}")
else:
    print("Debes ingresar un número entero positivo.")
