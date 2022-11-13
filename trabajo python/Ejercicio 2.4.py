#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo
#contrario devuelve False.
a=input()

def voc(jum):

    if jum=="a" or jum=="e" or jum=="i" or jum=="u" or jum=="u":
        x="Son vocales"
        ver(x)
    else:
        x="No son vocales"
        ver(x)


def ver(x):
    print(x)
voc(a)
