#Definir una función superposicion() que tome dos listas y devuelva True si tienen al
#menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando
#el bucle for anidado
import random

def superposicion():
    lista1=["emilio","jose","juan"]
    lista2=["paco","jose","juan"]
    x=0
    for a in lista1:
        for b in lista2:
            if a==b:
                x=1

    if x==1:
        print("true")
    else:
        print("false")

superposicion()