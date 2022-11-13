#Ejercicio 2.15
#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

array=[]
for a in range(0,10):

    edad=int(input("Introduzca las 10 edades "))
    array.append(edad)


def cantidad(array):
    cont=0
    for b in array:
        if b > 20:
            cont=cont+1
    print(cont)






cantidad(array)