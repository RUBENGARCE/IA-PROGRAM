# Tarea PIA01 - Juego de Piedra, Papel o Tijera
import random

opciones = ["piedra", "papel", "tijera"]

victorias = 0
derrotas = 0
empates = 0

print("=== PIEDRA, PAPEL O TIJERA ===")
print("Escribe 'salir' para terminar")

while True:
    jugador = input("\nElige piedra, papel o tijera: ").lower().strip()

    if jugador == "salir":
        break

    if jugador not in opciones:
        print("Esa opción no vale, prueba otra vez.")
        continue

    ordenador = random.choice(opciones)
    print("El ordenador ha elegido:", ordenador)

    if jugador == ordenador:
        print("Empate")
        empates += 1
    elif (jugador == "piedra" and ordenador == "tijera") or \
         (jugador == "papel" and ordenador == "piedra") or \
         (jugador == "tijera" and ordenador == "papel"):
        print("¡Has ganado!")
        victorias += 1
    else:
        print("Has perdido")
        derrotas += 1

print("\n--- Resultado final ---")
print("Victorias:", victorias)
print("Derrotas:", derrotas)
print("Empates:", empates)