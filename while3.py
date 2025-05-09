n=int(input("ingrese un numero entero positivo: "))
#calcular factorial
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(f"el factorial de {n} es: {fact}")