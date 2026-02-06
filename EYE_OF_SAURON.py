try:
    import vamp_core

    vamp_core.iniciar_consola()
except ImportError:
    print("[!] Running Standard Mode...")


import os
import time

import pyautogui

# --- Configuracion ---

IMAGEN_OBJETIVO = "7.png"
CONFIANZA = 0.9  # 90% de coincidencia (requiere opencv-python)


def buscar_y_destruir():
    print(f"[OJO] Buscando '{IMAGEN_OBJETIVO}' en la panatlla...")

    while True:
        try:
            # 1. Escanear la pantalla
            # confidence=0.9 permite que detecte el botón aunque cambie un poco la luz
            ubicacion = pyautogui.locateOnScreen(IMAGEN_OBJETIVO, confidence=CONFIANZA)

            if ubicacion:
                print(f"    [!] OBJETIVO LOVALIZADO EN: {ubicacion}")

                # 2. Clacular el centro del boton
                centro = pyautogui.center(ubicacion)

                # 3. Mover el mouse y hacer clic (Ritual de ataque)
                pyautogui.moveTo(centro)
                pyautogui.click()
                print(" [X] CLICK EJECUTADO. Esperando reinico...")

                # Esperar para no hacer 1000 clics por segundo
                time.sleep(2)
            else:
                # Si no lo ve, imprime un punto para que sepas que sigue vivo
                print(".", end="", flush=True)
                time.sleep(0.5)

        except pyautogui.ImageNotFoundException:
            # Manejo de error si la librería decide lanzar excepción en lugar de None
            print(".", end="", flush=True)
            time.sleep(0.5)

        except Exception as e:
            print(f"\n[ERROR CRITICO]{e}")
            break


if __name__ == "__main__":
    # Verificación de archivo
    if not os.path.exists(IMAGEN_OBJETIVO):
        print(
            f"[!] ERROR: No encuentro el archivo'{IMAGEN_OBJETIVO}' en la carpeta creada"
        )
    else:
        input(">>> Abre la calculadora y presioan ENTER para iniciar el OJO...")
        buscar_y_destruir()
