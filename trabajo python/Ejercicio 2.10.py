#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio
#2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos
#más de 3 números o no sabemos cuántos números son. Escribir una función
#max_in_list() que tome una lista de números y devuelva el más grande.

lista=[1,5,2,35,72,4]
def max_in_list(lista):
    c=0
    for b in lista:
        if c == 0:
            c=b
        elif c < b:
            c=b







max_in_list(lista)