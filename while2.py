M=int(input("Digite un número entero positivo: "))

if M > 0:
    producto = 1
    contador = 0
    numero = 2
    
    while contador < M:
        producto *= numero
        contador += 1
        numero += 2
        
    print(f"El producto de los primeros {M} números pares es: {producto}")
else:
    print("Debes ingresar un número entero positivo.")
        
    