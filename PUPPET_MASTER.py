try:
    import vamp_core

    vamp_core.iniciar_consola()
except ImportError:
    print("[!] Running Standard Mode...")

import time

import pyautogui
import pyperclip


def titiritero_matematico():
    print("[INIT] TOMAS EL CONTORL DEL SISTEMA")

    # 1. ABRIR CALCULADORA (HACKER STYLE)
    # En lugar de buscar el icono, usamos Windows + R (Ejecutar)

    print(" [>]Abriendo Calculadora...")
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write("calc")
    pyautogui.press("enter")

    # Esperamos a que la calculadora abra (vital)

    time.sleep(2)

    # 2. INYECTAR DATOS
    # Vamos a calcular algo complejo: 1337 por 42
    ecuacion = "1337 * 42"
    print(f"    [>] Inyectando virus matematico: {ecuacion}")

    # Escribe como si fueras tu (interval=0.1 le da efecto humano)
    pyautogui.write(ecuacion, interval=0.1)
    pyautogui.press("enter")

    time.sleep(1)  # Esperar al resultado

    # 3. EXTRAER INFORMACIÓN (DATA HEIST)
    print("   [>] Robando resultado (Ctrl + C)...")

    # --- LA PARTE QUE FALTABA ---
    pyautogui.hotkey("ctrl", "c")

    resultado = pyperclip.paste()

    # 4. REPORTE FINAL
    print("-" * 30)
    print("    [X] Mision Cumplida.")
    print(f"    [!] Resultados Capturados: {resultado}")
    print("-" * 30)


if __name__ == "__main__":
    input(">>> Presiona ENTER y suelta el mouse/teclado...")
    titiritero_matematico()
