import datetime
import random
import time as t
import os

fecha = datetime.date.today()

print(f"bienvenido \n({fecha})")

def esperar (espera):
    while (espera >= 0):
        os.system("cls || clear")
    print(f"espera {i}")
    t.sleep(1)
    os.system("cls || clear")   

def adivinar(num_user, num_rdm):
    if num_user == num_rdm:
        t.sleep(3)
        print("adivinaste")
    else:
        print("no adivinaste")
    
def main ():
    num_alea = random.randint(1, 10)
    resp = "s"
    while resp.lower() != "n":
        num = input("ingresa número del 1 al 10: ")
        adivinar(int(num), num_alea)
        resp = input("desea jugar de nuevo? [s = si = n = no - R = reiniciar]: ")
main()