from colorama import init, Fore, Style
import time
import os

init(autoreset=True)

def iniciar_consola():
    """
    Protocolo de inicio de sesión estándar para todos los sistemas VAMP.
    """
    print(Fore.RED + Style.BRIGHT + "--- [ V.A.M.P. SYSTEMS ONLINE ] ---")
    time.sleep(0.5)
    print(Fore.GREEN + ">> ACCESS GRANTED.\n")
    