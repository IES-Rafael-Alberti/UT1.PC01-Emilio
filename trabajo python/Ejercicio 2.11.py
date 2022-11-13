#Ejercicio 2.11
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.


ls=["juan","pepe","farmacia","juan"]



def mas_larga(ls):
    x=0
    palabra=""
    for a in ls:
        if x < len(a):

            x=len(a)

            palabra=a
    return palabra



c=mas_larga(ls)
print(c)