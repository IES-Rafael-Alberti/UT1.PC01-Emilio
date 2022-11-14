# UT1.PC01


1º [CE. a] En primer lugar vamos a comprobar las características principales de los lenguajes de programación a través de los ejercicios prácticos que habéis realizado. Los ejercicios serán los siguientes:

### ● Debéis elegir 1 ejercicio de UT1.A00 Introducción a la programación - parte 1.


*Ejercicio 1.1*
~~~
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
~~~

### Javascript

Con el lenguaje de programacion **javascript** los if y la forma de declarar una variable es un poco distinta,le tenemos que indicar con *var* para poder declarar una variable no es como en python que podemos declararla sin poner var, despues los if en necesitan ir entre parentesis y con abrir y cerrar llaves para determinar lo que abarca el if es tambien muy similar a **php** y despues en la sentencia siempre tenemos que poner un **;** para cerrar la sentencia.
~~~
var "nombre de la variable n" = "cadena";
if (condición) {
   sentencia1;
} else if{
   sentencia2;
} else {
    sentencia3;
}
~~~
Aqui les muestro un ejemplo de como seria en python la declaracion de variables que le esta indicando que el valor sea string y tambien una definicion de funcion con un return, tambien para los operadores logicos para and utilizamos && y para or utilizamos ||
~~~
bCondition1 || (bCondition2 && bCondition3)
~~~

- - -
En javascript para mostrar cosas por pantall con el  *alert*
~~~
alert("lo que quieras mostrar por pantalla");
~~~
* * *

![python](/img/1.png)

### PHP
Con el lenguaje de programación **php** Se ejecuta un script PHP en el servidor y el resultado HTML sin formato se envía de vuelta al navegador.Un script PHP se puede colocar en cualquier parte del documento Un script PHP comienza  <?php  y termina con ?>: ,la declaracion de variables es muy distinta a javascript en este caso se le pone **$** delante de la variable para que pueda ser declarada y definida
~~~
<?php
$txt = "Hello world!";
$x = 5;
$y = 10.5;
?>
~~~
En caso de PHP para definir si es una cadena o un valor numerico, en formato cadena ponemos "" para indicar que es un string y en valor numerico sin comillas
~~~
$x = "Hello world!";
$y =  563424;
~~~
Para los **IF** es muy similar al javascript tambien podemos poner los operadores logicos como && y || que son and y or 
~~~
<?php
$t = 5;

if ($t < 10 && t > 0) {
  echo "es menor";
}else{
    condicion
}
?>
~~~
el *echo* en php sirve para mostrar un comentario, es como poner un *print* en python

### ● Debéis elegir 2 ejercicios de UT1.A00 Introducción a la programación - parte 2.

Ejercicio 2.2
~~~
print("Escriba 3 numeros")
num1=input()
num2=input()
num3=input()
def mayor_3(num1,num2,num3):
    if num1 > num2:

       var=num1
    elif(num2>num1):

        var=num2
    else:
        var=num1
    if (var > num3):
      print(f'el numero {var} es mayor de los tres')
    else:
      print(f'el numero {num3} es mayor de los tres')
mayor_3(num1,num2,num3)
~~~
Ejercicio 2.5
~~~
a=[2,4,1,4,5,1]


def mult(b):
    mul=1
    for a in b:
        mul=mul*a
    ver1(mul)

def sum(b):
    sum=0
    for a in b:
        sum=sum+a
    ver2(sum)

def ver1(vis):
    print(f'La multiplicacion da {vis}')
def ver2(vis):
    print(f'La suma da {vis}')

mult(a)
sum(a)
~~~

Estos dos ejercicios:
- - -
### javascript

javascript para mostrar algo por pantalla utiliza el alert, los if necesitan ser abiertos y cerrados con llaves y cada sentencia tiene que estar cerrada con *;* 

ejemplo de una funcion en javascript:
~~~
let x = myFunction(4, 3);   // Aqui hacemos la llamada a la funcion
function myFunction(a, b) {
  return a * b;             // la funcion multiplica a y b y lo retorna a x
}
~~~
para poder crear un array en javascript es muy distinto a php o pyhton 
~~~
let frutas = ["Manzana", "Banana"]
 // La instrucción let declara una variable de alcance local con ámbito de bloque
~~~

Los if estan explicado en la practica anterior que son identicos y los operandos de mayor que y menor que son iguales en ambos aspectos
- - -
### PHP
para declarar arrays en php es de la siguiente forma muy diferentes los 3 lenguajes entre si y siempre con la sentencia alfinal terminado en *;*
~~~
$cars = array("Volvo", "BMW", "Toyota");
~~~
Para las llamadas a las funciones
~~~
function writeMsg() {
  echo "Hello world!";
}

writeMsg(); // LLamada a la funcion
~~~
---
Caracteristicas

PHP

- Código abierto
- Simple y facil de usar
- Soporte de multiples bases de datos
- compatibilidad multiplataforma
- flexible
- Reporte de errores y manejo de excepciones
- Rendimiento eficiente y rapido
- Monitorizacion en tiempo real
- caracterisiticas orientadas a objetos

Javascript

- Lenguaje orientado a objetos
- No tipado
- De alto nivel
- Lenguaje interpretado
- Muy utilizado por desarrolladores
- - - 

### En esta actividad vamos a realizar una comparación entre Python y C, es por ello quedebes elegir tres de los ejercicios de los realizados en clase y contestar a las siguientes preguntas.

Programa utilizado
Ejercicio 2.12
~~~
entero=input("ponga un dato: ")

def filtrar_palabra():
    lista=["farmacia","pepe","josefa"]
    palabra=""
    for a in lista:
        if int(entero)<len(a):
            palabra+=" "+a

    return palabra
print(filtrar_palabra())
~~~
Ejercicio 2.16
~~~
array=["prueba","casa","Emilio","Emi","pepe"]
p=input("inserta la letra: ")

if   1 < len(p):

    print("error")

else:

    for a in array:
        if p == a[0]:
            print(a)


~~~
Ejercicio 2.17
~~~
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
~~~

## **● ¿Qué diferencias habría en el desarrollo del programa?**

Primero tendramos que declarar nuestra biblioteca de C con #include **<stdio.h>**

luego abririamos nuestra funcion principal **int main() {...}**

a la hora de declarar las variables tambien le tendriamos que poner el tipo de variable que estamos definiendo

~~~
tipo nombredevariable = valor;

int myNum = 15; /asi 
int myNum;
myNum = 15; / tambien fucniona de esta manera
~~~
Los tipos de datos en C son muy distintos a python cuando nostros teniamos una cadena lo poniamos como valor string en este caso en C es char

![imagen.2](/img/2.png)

---
El printf nos permite mostrar por pantalla igual que lo haria el print

~~~
printf("Hello World!");
~~~

El if sigue siendo igual tambien en C

Ejemplo
~~~
if (condition1) {
  
} else if (condition2) {
 
} else {
 
}
~~~

Tanto en C y en Python se puede utilizar el **for** y el **while**

~~~
for (statement 1; statement 2; statement 3) {
 
}
~~~
El array es muy similar a python igual, en C tenemos que determinar que tipo de array es si es int o char... 

~~~
int myNumbers[] = {25, 50, 75, 100};
~~~

Lo que cambia del input en python y en C

~~~
// Creamos una variable que guarda el numero del usuario
int myNum;

//preguntamos al usuario que escriba un numero
printf("Type a number: \n");

// guardamos el numero
scanf("%d", &myNum);

// y sacamos el numero escrito
printf("Your number is: %d", myNum);
~~~

Esta seria la diferencia en el desarrollo del programa a la hora de estructurarlo y escribirlo


--- 

## **● ¿Qué diferencias existen entre los dos lenguajes?**

C es un lenguaje de programación estructural, mientras que Python es un lenguaje de programación orientado a objetos.

Python es un lenguaje de programación de propósito general, mientras que C se usa principalmente para aplicaciones relacionadas con hardware y código de bajo nivel.

C es un lenguaje compilado y Python es un lenguaje interpretado.
La ejecución de código es más rápida en C que en Python.

Python no admite la funcionalidad de puntero, pero los punteros están disponibles en C.

C tiene una biblioteca limitada de funciones integradas, mientras que Python es más extensa.

En C, es obligatorio declarar tipos de variables, pero esto no es necesario en Python.

C permite la asignación de líneas, mientras que da errores en Python.

La sintaxis de Python es más fácil de entender que la de C.

## **● ¿Para qué tipo de programa puede servir cada lenguaje?**

Python es ampliamente utilizado por empresas de todo el mundo para construir aplicaciones web, analizar datos, automatizar operaciones y crear aplicaciones empresariales fiables y escalables es de interpretado.

C se usó tanto para definir el sistema operativo como para definir el compilador como para crear los programas que funcionaban en UNIX. C se popularizó como lenguaje útil y potente, utilizable bajo cualquier sistema operativo o hardware, se desarrollan tanto aplicaciones como sistemas operativos a la vez que forma la base de otros lenguajes más actuales como Java, C++ o C#.

---


## **● ¿Cómo sería el proceso de lectura del código fuente de cada programa?**

En los tres programas en C tendriamos que crear un funcion **Main** que es la principal donde se ejecuta ya a raiz de eso es igual que python ya que son compiladores, la compilacion pasa por 3 fases Preprocesado, Compilación y Enlazado

**Ejercicio 1.12**

El codigo empezaria con la funcion Main predominando dentro de la funcion Main iria un **printF** que pida los datos y con un **Scanf** que guarde los datos de la variable  luego hariamos una funcion que se llame filtrar_palabra con un array y un for dentro con un if y luego haremos un **printf**

**Ejercicio 2.16**

Empezamos con una funcion Main principal y luego dentro de la misma hacemos un array, con scanf y prinf le pedimos que ingrese un valor luego con un fi y else normal con las condiciones y listo

**Ejercicio 2.17**

Empezamos otra vez con una funcion main que predomina, luego dentro creamos otra funcion contar_vocales que contendra dentro un array y un for 


 ## Teniendo todos los ejercicios realizados y entregado. Sobre el código fuente creado en la relación de ejercicios de las actividades 0 y 1 de la unidad, realiza en un documento los comentarios sobre todos los ejercicios indicando que elementos del código fuente has utilizado y qué función tienen.

 Elementos utilizados:


Input Introducir un valor por pantalla
~~~
p=input("inserta la letra: ")
~~~
print muestra por pantalla el valor o variable indicada
~~~
print(x)
~~~
arrays o lista para guardar varios valores en una lista
~~~
a=[2,4,1,4,5,1]
~~~
if condiciones
~~~
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
~~~
for sirve para hacer bucles igual que el while
~~~
for a in b:
        sum=sum+a
for c in range(0,10):
~~~
while
~~~
i = 1
while i < 6:
  print(i)
  i += 1
~~~
definicion de funciones y llamadas a la funcion
~~~
def mayor_3(num1,num2,num3):
mayo_3
~~~
Caracter aleatorio: te genera un numero aleatorio en el rango indicado del 0 al 100
~~~
 n=random.randint(0,100)
~~~
la funcion len sirve para contar cuantos caracteres tiene una variable o un dato
~~~
len(a)
~~~
Concatenar
~~~
palabra+=" "+a
~~~
agregar mas valores a un array
~~~
array.append(edad)
~~~