#Definir un histograma procedimiento() que tome una lista de números enteros e
#imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir
#lo siguiente:

lista=[10,10,100,100,10,10]
def procedimiento():
    c =""
    for a in lista:
        for b in range (0,a):
            c=c+"*"
        print(c)
        c=""



procedimiento()