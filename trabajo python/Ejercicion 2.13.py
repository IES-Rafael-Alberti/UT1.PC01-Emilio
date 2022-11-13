#Ejercicio 2.13
#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
#que evaluar la cadena y decir cuantas letras mayúsculas tiene.

frase=str(input("inserta la frase deseada: "))


def pala(frase):
    cont=0
    for a in frase:
        j=str(a.isupper())

        if "True" == j :
            cont = cont + 1



    return cont


ver=pala(frase)

print(ver)