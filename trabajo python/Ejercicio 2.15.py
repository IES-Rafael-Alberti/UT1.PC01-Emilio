#Ejercicio 2.15
#Definir una tupla con 10 edades de personas.
#Imprimir la cantidad de personas con edades superiores a 20.
#Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

tup=(21,24,3,10,5,1,6,2,0,5)
con=0
for a in range(0,9):



    if tup[a] > 20:
     con=con+1


print(con)



