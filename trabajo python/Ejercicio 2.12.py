#Ejercicio 2.12
#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
#devuelva las palabras que tengan más de n caracteres.

entero=input("ponga un dato: ")

def filtrar_palabra():
    lista=["farmacia","pepe","josefa"]
    palabra=""
    for a in lista:
        if int(entero)<len(a):
            palabra+=" "+a

    return palabra
print(filtrar_palabra())