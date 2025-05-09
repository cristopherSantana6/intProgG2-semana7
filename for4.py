n= int(input("ingrese la cantidad de calificaciones: "))
suma=0
cont=0
for i in range(n):
    calif= float(input("ingrese la calificacion: "))
    suma+=calif
    cont+=1
promedio= suma/cont
print(f"el promedio de las calificaciones es: {promedio}")
if promedio >= 70:
    print("aprobado")
else:
    print("reprobado")
