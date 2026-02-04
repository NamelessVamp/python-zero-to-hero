import random
import time
import string

print("[SYSTEM] Cargando libreria VAMP_UTILS v1.0 ...")

#1. Funcion SImple (Return)
def tirar_dado(caras=6):
    """
    Simula tirar un dado de RPG.
    Si no dices cuantas caras, usa 6 por defecto
    """
    resultado = random.randint(1, caras)
    return resultado

#2 Funcion con Logica (Generador)
def generar_password(longitud=8):
    """
    Genera una contraseña segura al azar.
    Usa letras mayúsculas, minúsculas y números.
    """

    caracteres = string.ascii_letters + string.digits #abc...ABC...123
    password= ""

    #Elegimos 'longitud' veces un caracter al azar 
    for i in range(longitud):
        password += random.choice(caracteres)

    return password
    
#3 Funcion de efecto visual (Void - no devuelve nada, solo hace)
def efecto_typing(texto, velocidad = 0.05):
    """
    Docstring para efecto_typing

    """

    for letra in texto:
        print(letra, end="", flush=True) #flush fuerza a imprimir al instante
        time.sleep(velocidad)
    print()