import os
import time
import json # <--- Nuevo: libreria para guardar archivos reales
from colorama import init, Fore, Back, Style #<---- Nuevo Arsenal

init(autoreset=True)

ARCHIVO_DATOS = "player_data.json"

# --- 1 La Clase (El Protagonista) ---
class Agente:
    def __init__(self, nombre, nivel=1, xp=0):
        self.nombre = nombre
        self.nivel = nivel
        self.xp = xp
        self.xp_para_subir = 100

    def ganar_xp(self, cantidad):
        print(Fore.CYAN + f"\n[+] Ganaste {cantidad} XP!")
        self.xp += cantidad

        #Check de Nivel
        while self.xp >= self.xp_para_subir:
            self.xp -= self.xp_para_subir
            self.nivel += 1
            print(Fore.GREEN + Style.BRIGHT + f"LEVEL UP! Ahora eres nivel {self.nivel}")
            print(Fore.GREEN + "Tu capacidad de procesamiento ha aumentado.")
            time.sleep (1)

    def mostrar_status(self):
        barra = "█" * (self.xp //10) + "-" * ((100 - self.xp) //10)
        print(f"\nAGENTE: {Fore.YELLOW}{self.nombre} {Style.RESET_ALL}| LVL: {Fore.GREEN}{self.nivel}")
        print(f"XP: [{Fore.RED}{barra}] {self.xp/100}")

# --- 2. FUNCIONES DE PERSISTENCIA (Guardar/Cargar) ---

def guardar_progreso(agente):
    #Convertimos el objeto a diccionario para que JSON lo entienda
    datos = {
        "nombre": agente.nombre,
        "nivel": agente.nivel,
        "xp":agente.xp
    }

    #Escribimos en el disco duro
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(datos, archivo)
    print("Progreso guardado en disco")

def cargar_progreso():
    #intentamos leer el archivo si existe 
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r") as archivo:
            datos = json.load(archivo)
        print (" Archivo de guardado encontrado. Cargando...")
        return Agente(datos["nombre"], datos["nivel"], datos["xp"])
    else:
        print("No hay datos guardados. Creando un nuevo perfil...")
        nombre = input ("Ingresa tu alias: ")
        return Agente (nombre)
    
# --- 3. EL BUCLE PRINCIPAL (Main Loop) ---
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---[ TASK RPG: GAMIFY YOUR LIFE ]---")

    #paso1: Cargar o crear personaje
    player = cargar_progreso()
    time.sleep(1)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        player.mostrar_status()

        print("\n--- MISSION BOARD ---")
        print("1. Completar Tarea Facil (10 XP)")
        print("2. Commpletar Tarea Media (20 XP)")
        print("3. Completar Tarea Hardcore (50XP)")
        print("4. Guardar y salir")

        opcion = input("\n>>> Selecciona operacion: ")

        if opcion == "1":
            print("Completando tarea simple...")
            time.sleep(1)
            player.ganar_xp(10)

        elif opcion == "2":
            print("Resolviendo problema tecnico...")
            time.sleep(1.5)
            player.ganar_xp(20)

        elif opcion == "3":
            print("Hackeando servidor corporativo...")
            #efecto de carga falso jej
            for i in range (3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            player.ganar_xp(50)

        elif opcion == "4":
            guardar_progreso(player)
            print("Desconectando del sistema...")
            break
        
        else:
            print("Comando invalido")

        input("\b[Presiona enter para continuar]")

#--- Punto de entrada --- 
if __name__ == "__main__":
    main()