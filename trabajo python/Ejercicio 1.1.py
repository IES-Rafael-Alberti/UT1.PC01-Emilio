#Ejercicio 1.1
# El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
#El usuario proporcionará un valor entre 0 y 10.
#Si está entre 9 y 10: imprimir una A
#Si está entre 8 y menor a 9: imprimir una B
#Si está entre 7 y menor a 8: imprimir una C
#Si está entre 6 y menor a 7: imprimir una D
#Si está entre 0 y menor a 6: imprimir una F
#cualquier otro valor debe imprimir: Valor desconocido

a=int(input("Introduzca valor:"))

if str(a) not in '0123456789':
    print("Valor Desconocido")
    pass
else:
    if a >= 9 and a <= 10:
        print("A")
    elif a >= 8 and a <= 9:
        print("B")
    elif a >= 7 and a <= 8:
        print("C")
    elif a >= 6 and a <= 7:
        print("D")
    elif a >= 0 and a <= 6:
        print("E")