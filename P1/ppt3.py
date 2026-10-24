# Tarea PIA01 - Piedra, Papel o Tijera
import random

print("Piedra, papel o tijera")
jugador = input("Escribe piedra, papel o tijera: ")

ordenador = random.choice(["piedra", "papel", "tijera"])
print("El ordenador eligió:", ordenador)

if jugador == ordenador:
    print("Empate")
elif jugador == "piedra" and ordenador == "tijera":
    print("Ganaste")
elif jugador == "papel" and ordenador == "piedra":
    print("Ganaste")
elif jugador == "tijera" and ordenador == "papel":
    print("Ganaste")
else:
    print("Perdiste")