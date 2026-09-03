#Librerias
import turtle
import random

#Ajuste de pantalla
screen = turtle.Screen()
screen.setup(width=900, height=500)
screen.bgcolor("black")
screen.title("DVD Practica")

#Desactivar animacion automatica
turtle.tracer(0)

#Logo
logo = turtle.Turtle()
logo.hideturtle()

#Pocision inicial
x = 0
y = 0

#Velocidad de movimiento
dx = 3
dy = 2

#Colores
colors = ["red", "green", "blue", "yellow", "purple", "orange", "white"]

def color_change():
    logo.color(random.choice(colors))

color_change()

#Animacion

while True:
    #borrar logo
    logo.clear()

    logo.goto(x,y)

    logo.write("DVD", align="center", font=("Arial", 24, "bold"))

#Movimiento
    x += dx
    y += dy

#Colision con los bordes
    if x > 400 or x < -400:
        dx *= -1
    color_change() 

    if y > 200 or y < -200:
        dy *= -1
    color_change()

    #Actualizar pantalla
    screen.update()
    screen.ontimer(lambda: None, 10)

