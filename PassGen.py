import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

longitud = int(input("Introduce la longitud de la contraseña: "))
print("Contraseña generada:", generar_contraseña(longitud))
