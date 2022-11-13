#Ejercicio 2.16
#Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
#letra a.
#También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)

array=["prueba","casa","Emilio","Emi","pepe"]
p=input("inserta la letra: ")

if   1 < len(p):

    print("error")

else:

    for a in array:
        if p == a[0]:
            print(a)

