import random 
import time

def search_bin(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
        return -1 
    MiLista = [1, 2, 3, 4, 5, 10, 12]
    
    print(search_bin(MiLista, 10))