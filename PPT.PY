"""
Tarea PIA01 - Juego de Piedra, Papel o Tijera
IABD - Programación de Inteligencia Artificial
UT01 - Introducción a la programación de Inteligencia Artificial
"""
import random
# 1. Constantes
ROCK = "piedra"
PAPER = "papel"
SCISSORS = "tijera"
OPCIONES = {
# Tarea PIA01 · Piedra, Papel o Tijera · Página 1
    "1": ROCK,
    "2": PAPER,
    "3": SCISSORS,
}
def decidir_ganador(user_action, computer_action):
    """Compara las dos jugadas e imprime el resultado de la ronda.
    Devuelve 'usuario', 'ordenador' o 'empate'."""
    if user_action == computer_action:
        print(f"Ambos habéis elegido {user_action}. ¡Empate!")
        return "empate"
    if user_action == ROCK:
        if computer_action == SCISSORS:
            print("La piedra rompe la tijera. ¡Ganaste!")
            return "usuario"
        else:
            print("El papel envuelve la piedra. Perdiste.")
            return "ordenador"
    elif user_action == PAPER:
        if computer_action == ROCK:
            print("El papel envuelve la piedra. ¡Ganaste!")
            return "usuario"
        else:
            print("La tijera corta el papel. Perdiste.")
            return "ordenador"
    elif user_action == SCISSORS:
        if computer_action == PAPER:
            print("La tijera corta el papel. ¡Ganaste!")
            return "usuario"
        else:
            print("La piedra rompe la tijera. Perdiste.")
            return "ordenador"
def pedir_jugada():
    """Pide la jugada al usuario hasta que introduzca una opción válida."""
    while True:
        eleccion = input("\nElige: 1) piedra  2) papel  3) tijera  -> ").strip()
        if eleccion in OPCIONES:
            return OPCIONES[eleccion]
        print("Opción no válida. Introduce 1, 2 o 3.")
def main():
    print("=== PIEDRA, PAPEL O TIJERA ===")
    print("(Pulsa Ctrl + C para salir)")1
    victorias = derrotas = empates = 0
    try:
        while True:
            user_action = pedir_jugada()
            computer_action = random.choice([ROCK, PAPER, SCISSORS])
            print(f"Tú: {user_action} | Ordenador: {computer_action}")
            resultado = decidir_ganador(user_action, computer_action)
            if resultado == "usuario":
                victorias += 1
            elif resultado == "ordenador":
                derrotas += 1
            else:
                empates += 1
    except (KeyboardInterrupt, EOFError):
        print("\n\n--- Fin de la partida ---")
        print(f"Victorias: {victorias} | Derrotas: {derrotas} | Empates: {empates}")
# Punto de entrada
if __name__ == "__main__":
    main()