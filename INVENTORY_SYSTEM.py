import time
import os #para limpiar la pantalla

#1 Inicializacion (La mochila Vacia)

inventario = ["CyberDeck", "Pistola 10mm"] #Empezamos con items base
capacidad_max=5

def limpiar_pantalla():
    #Pequeño truco: cls apra windows, Clear para Linux y Mac
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_pantalla()
print("---[V.A.M.P INVENTORY MANAGMENT SYSTEM]---")

#2 El game Loop(El Corazon del Programa)

while True:
    print(f"\n[SLOTS OCUPADOS: {len(inventario)}/{capacidad_max}]")
    print("COMMANDS: [ADD] [SHOW] [DROP] [EXIT]")
    accion = input(">>>AWAITING INPUT<<<").upper() #.upper() cnovierte a mayusculas las letras

    #---Comando: Mostrar---
    if accion == "SHOW":
        print("\n--- Mochila Actual ---")
        #Usamos un FOR para recorrer la lista item por item 
        for item in inventario:
            print(f"-[X]{item}")
        print("----------------------")

    #--- COMANDO: Agregar---

    elif accion == "ADD":
        if len(inventario) < capacidad_max:
            nuevo_item = input("Nombre del objeto a Lootear: ")
            inventario.append(nuevo_item)# <--- AQUÍ OCURRE LA MAGIA
            print(f"{nuevo_item} agregado al inventario")
        else:
            print("Mochilla Llena. Tienes que soltar algo.")

    #--- COMANDO: Tirar---
    elif accion == "DROP":
        item_a_borrar = input("Que Objeto vas a tirar: ")

        #primero verificamos si existe (para evitar errores)
        if item_a_borrar in inventario:
            inventario.remove(item_a_borrar) #Eliminacion
            print(f"{item_a_borrar} eliminado")
        else:
            print("Ese objeto no esta en tu inventario")
    
    #---Comando: Salir---
    elif accion == "EXIT":
        print ("Guardando datos...(Mentira, se perderan al cerrar XD)")
        time.sleep(1)
        print("OFFLINE.")
        break

    else:
        print("Comando Desconocido")