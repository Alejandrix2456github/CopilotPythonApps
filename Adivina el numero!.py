import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

adivina_el_numero()