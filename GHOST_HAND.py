try:
    import vamp_core
    vamp_core.iniciar_consola()
except ImportError:
    print("[!] Running Standard Mode...")

import pyautogui
import time
import os
from colorama import Fore, Style

# --- CONFIGURACIÓN DE SEGURIDAD (FAIL-SAFE) ---
#Si llevas el mouse a la esquina (0,0) el script muere.
pyautogui.FAILSAFE = True
#Pausa de 1 segundo entre cada accion para que puedas ver que hace
pyautogui.PAUSE = 1.0

def ritual_de_escritura():
    """
    # DEUS EX MACHINA
    Controla el teclado físico para invocar el Bloc de Notas.
    """
    
    print(Fore.CYAN + "[*] Iniciando secuensa de posesion de hardware...")
    
    
    #1 Presionar la tecla de Windows

    print(Fore.YELLOW + "   > Abriendo Menú Inicio...")    
    pyautogui.press('win')
    
    #2 Escribir 'Notepad' y dar enter
    print(Fore.YELLOW + "   > Buscando Objetivos...")
    pyautogui.write('notepad', interval = 0.1)# interval simula velocidad humana
    pyautogui.press('enter')
    
    #esperamos a que abra el programa (Vital en automatizacion)
    print(Fore.CYAN + "[*] Esperando Interfaz Visual (2s)...")
    time.sleep(2)
    
    #3 Escribir el mensaje
    print(Fore.MAGENTA + "  > Inyectando payload de texto...")
    mensaje =("Hola, Vamp. Soy Python. He tomado el control de tu DELL.")
    
    #Typewrite escribe letra por letra
    pyautogui.write(mensaje, interval=0.05)
    
    #4 Firma Final
    pyautogui.press('enter')
    pyautogui.write("-- Ghost Protocol Complete --")
    
    print(Fore.GREEN + Style.BRIGHT + "\n [+] Mision Cumplida, control retornado al usuario")

if __name__ == "__main__":
    #Preguntar antes de ejecutar por seguridad
    input(Fore.RED + ">>> Estas listo para soltar el mouse? Presiona Enter...")
    ritual_de_escritura()