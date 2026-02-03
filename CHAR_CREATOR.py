import datetime

#1. INPUT (recolección de datos)
#La función de  Input () Siempre devuelve el texto (str)
print("---[INITIALIZING CHARACTER CREATION]---")
nombre = input("Ingresa tu Alias: ")
rol = input("Clase (Netrunner/Solo/Techie): ")

# OJO: input() devuelve texto. Debemos convertirlo a Numero (int) para restar.

anio_nacimiento = input("Año de Nacimiento: ")
anio_nacimiento = int(anio_nacimiento) # Casting: Convertir str a int 

#2. Proceso (lógica Interna)
anio_actual = 2026
edad = anio_actual - anio_nacimiento

#Variables flotantes y booleanas
nivel_hacking = 1.5 #Empiezas como Noob
status_vivo = True

#3 Output(Renderizado)

print("\n"*2)
print("╔════════════════════════════════╗")
print(f"║Identity: {nombre.upper()}")# .upper() hace mayúsculas
print(f"║Class: {rol.capitalize()}")# .capitalize() pone la 1ra mayúscula
print("╠────────────────────────────────╣")
print(f"║AGE: {edad} years old")
print(f"║HACK_LVL: {nivel_hacking} v")
print(f"║ALIVE: {status_vivo}")
print("╚════════════════════════════════╝")