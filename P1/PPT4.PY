# Tarea PIA01 - Piedra, Papel o Tijera
import random

# Constantes
piedra = "piedra"
papel = "papel"
tijeras = "tijera"


def decidir_ganador(user_action, computer_action):
    if user_action == computer_action:
        print("Empate")
    elif user_action == ROCK:
        if computer_action == SCISSORS:
            print("Ganaste")
        else:
            print("Perdiste")
    elif user_action == PAPER:
        if computer_action == ROCK:
            print("Ganaste")
        else:
            print("Perdiste")
    elif user_action == SCISSORS:
        if computer_action == PAPER:
            print("Ganaste")
        else:
            print("Perdiste")


def main():
    print("Piedra, papel o tijera (escribe 'salir' para terminar)")
    while True:
        user_action = input("\nElige piedra, papel o tijera: ").lower()

        if user_action == "salir":
            break

        if user_action not in [ROCK, PAPER, SCISSORS]:
            print("Opción no válida")
            continue

        computer_action = random.choice([ROCK, PAPER, SCISSORS])
        print("El ordenador eligió:", computer_action)
        decidir_ganador(user_action, computer_action)


if __name__ == "__main__":
    main()
