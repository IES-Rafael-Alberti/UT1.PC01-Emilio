#Ejercicio 2.17
#Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
#tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.


palabra=input("introduzca palabra: ")

def contar_vocales(palabra):
    lista=["a","e","i","o","u","A","E","I","O","U"]
    for b in lista:
        cont=0
        for a in palabra:
            if a == b:
                cont=cont+1
        if cont > 0:
            print(f"la vocal {b} se repite {cont}")





contar_vocales(palabra)





