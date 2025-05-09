## leer una palabra diferente a fin y converturla a mayusculas

palabra = input("Escribe una palabra: ")
fin= "fin"

for i in range(10000000):
    if palabra.lower() == "fin":
        break
    else: 
        print(f"{palabra.upper()} tiene {len(palabra)} letras")
        palabra = input("Escribe una palabra: ")