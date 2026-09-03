#Librerias
import turtle
import random

#Ajustes de la ventana
screen = turtle.Screen()
screen.setup(900, 500)
screen.bgcolor("black")
screen.title("DVD")
screen.tracer(0)

# Diseño del Logo
logo = turtle.Turtle()
logo.hideturtle()
logo.penup()
#Variables de movimiento y posición
x = 0
y = 0
dx = 3
dy = 2

# COLORES

colores = ["red","blue","green","yellow","purple","cyan","orange","white"]

logo.color(random.choice(colores))

#Animacion

def animar():

    global x, y, dx, dy

    logo.clear()

    # Dibujar logo
    logo.goto(x, y)

    logo.write(
        "DVD",
        align="center",
        font=("Arial", 40, "bold")
    )

    # Movimiento
    x += dx
    y += dy

    # Límites
    if x >= 400 or x <= -400:
        dx *= -1
        logo.color(random.choice(colores))

    if y >= 200 or y <= -200:
        dy *= -1
        logo.color(random.choice(colores))

    # Actualizar
    screen.update()

    # Volver a ejecutar después de 10 ms
    screen.ontimer(animar, 10)


# Iniciar
animar()

# Mantener ventana abierta
screen.mainloop()