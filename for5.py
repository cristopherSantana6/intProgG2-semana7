#contar palabras en una frase  Enunciado: Pide al usuario una frase y cuenta el número de palabras que contiene.  
# Especificación: Usa un bucle for (o métodos de string) y un contador. 

frase=input("Ingrese una frase: ")
palabras=frase.split()

contador=0
for palabra in palabras:
    contador+=1
print(f"La frase contiene {contador} palabras.")





