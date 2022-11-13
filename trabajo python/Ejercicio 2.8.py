#Definir una función generar_n_caracteres() que tome un entero n y devuelva el
#caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver
#"xxxxx".
import random

def generar_n_caracteres():
    n=random.randint(0,100)
    con=""
    for x in range (0,n):
        con=con+str(n)

    print(con)

generar_n_caracteres()