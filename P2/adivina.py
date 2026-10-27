# Adivina el número
import random

MINIMO = 1
MAXIMO = 20
INTENTOS = 5


def pedir_numero():
    while True:
        texto = input("Tu número: ")
        if texto.isdigit() and MINIMO <= int(texto) <= MAXIMO:
            return int(texto)
        print(f"Escribe un número entre {MINIMO} y {MAXIMO}")


def jugar():
    secreto = random.randint(MINIMO, MAXIMO)
    print(f"\nHe pensado un número entre {MINIMO} y {MAXIMO}. Tienes {INTENTOS} intentos.")

    for intento in range(1, INTENTOS + 1):
        numero = pedir_numero()

        if numero == secreto:
            print(f"¡Correcto! Lo has adivinado en {intento} intento(s).")
            return
        elif numero < secreto:
            print("Más alto")
        else:
            print("Más bajo")

    print(f"Te has quedado sin intentos. Era el {secreto}.")


def main():
    print("=== ADIVINA EL NÚMERO ===")
    while True:
        jugar()
        seguir = input("\nPulsa X para salir o Enter para jugar otra vez: ").lower()
        if seguir == "x":
            break
    print("¡Hasta la próxima!")


if __name__ == "__main__":
    main()