import random
import turtle

# Configuración de la ventana
screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)

# Configuración de la tortuga
t = turtle.Turtle()
t.speed(0)

# Dibujar
for x in range(300):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    t.color(r, g, b)
    t.forward(x * 10)
    t.right(91)

# Mantener la ventana abierta
turtle.done()