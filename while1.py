## leer una palabra diferente a fin y converturla a mayusculas

palabra = input("Escribe una palabra: ")
while palabra.lower() != "fin":
    print(f"{palabra.upper()} tiene {len(palabra)} letras")
    palabra = input("Escribe una palabra: ")

else :
    print("adios...")