# Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto
# que python tiene la función len() incorporada, pero escribirla por nosotros mismos
# resulta un muy buen ejercicio.

lista = ['a', 'b', 'd', 'i', 'j']

def contador(dato):
    total=0
    for a in dato:
        total+=1

    print(f"Los datos en la lista son {total}")
contador(lista)
