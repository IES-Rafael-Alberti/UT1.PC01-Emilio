import turtle
import time

# Movimiento de curva
def curveMove():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)




def drawHeart():
    turtle.speed(100) # La velocidad del cepillo se ajusta al máximo
    turtle.color('red','pink')
    turtle.begin_fill()
   # turtle.left(140) # Gire 140 grados en sentido antihorario
    turtle.forward(300.300) # Avanzar 111,65 píxeles
   # turtle.left(180)
    curveMove() # Dibuja una curva
    turtle.forward(300.300)  # Avanzar 111,65 píxeles

    turtle.left(-360) # Gire 120 grados en sentido antihorario
    curveMove() # Continuar dibujando la curva
    turtle.left(-360)
    curveMove()  # Continuar dibujando la curva
ç
   # turtle.forward(111.65) # Avanzar 111,65 píxeles

    turtle.end_fill()
    time.sleep(10)

if 0 == 0:
    drawHeart()