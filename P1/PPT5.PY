# Tarea PIA01 - Piedra, Papel o Tijera
import random

# Constantes
PIEDRA = "piedra"
PAPEL = "papel"
TIJERA = "tijera"


def decidir_ganador(user_action, computer_action):
    if user_action == computer_action:
        print("Empate")
    elif user_action == PIEDRA:
        if computer_action == TIJERA:
            print("Ganaste")
        else:
            print("Perdiste")
    elif user_action == PAPEL:
        if computer_action == PIEDRA:
            print("Ganaste")
        else:
            print("Perdiste")
    elif user_action == TIJERA:
        if computer_action == PAPEL:
            print("Ganaste")
        else:
            print("Perdiste")


def main():
    print("Piedra, papel o tijera")
    while True:
        user_action = input("\nElige piedra, papel o tijera: ").lower()

        if user_action not in [PIEDRA, PAPEL, TIJERA]:
            print("Opción no válida")
            continue

        computer_action = random.choice([PIEDRA, PAPEL, TIJERA])
        print("El ordenador eligió:", computer_action)
        decidir_ganador(user_action, computer_action)

        seguir = input("\nPulsa X para salir o Enter para continuar: ").lower()
        if seguir == "x":
            break


if __name__ == "__main__":
    main()
