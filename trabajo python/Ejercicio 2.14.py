#Ejercicio 2.14
#Construir un pequeño programa que convierta números binarios en enteros.
#Ejercicio 6
#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.


op=int(input("Opcion 1 o 2:"))
if op == 1 :
    bi=input("Escriba su numero en binario: ")

    entero = int(bi,base=2)

    print(entero)
elif op == 2 :
    array=[]
    año=int(input("ingresa el año en curso: "))
    for a in range (0,3):
        nombre=input("introduzca su nombre: ")
        fech=int(input("Introduzca su año de nacimiento "))
        años=año-fech
        array.append("usted es "+nombre+" y tiene "+str(años)+" años")

    for b in array:
        print(b)


