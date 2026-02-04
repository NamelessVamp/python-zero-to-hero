import time 

class CyberPet:
    #1 El constructor(El Nacimiento)
    #Se ejecuta automaticamente al crear el objeto
    def __init__(self, nombre_elegido):
        self.nombre = nombre_elegido
        self.energia = 100
        self.felicidad = 50
        print(f"Sistema: Ha nacido {self.nombre}!")

    #2 Metodos
    def status(self):
        print(f"\nEstado de {self.nombre.upper()}")
        print(f"Energia: {self.energia}%")
        print(f"Felicidad: {self.felicidad}%")
        print("-"*20)

    def jugar(self):
        if self.energia > 10:
            print(f"{self.nombre} esta jugando doom...")
            self.energia -=20 #se cansa
            self.felicidad += 15 #se pone feliz
            time.sleep(1)
        else:
            print(f"{self.nombre} esta muy cansado para jugar")

    def alimentar(self):
        print(f"Dando Ram y Datos a {self.nombre}...")
        self.energia += 30
        self.felicidad += 5
        #Evitamos que pase de 100
        if self.energia > 100:
            self.energia = 100
        time.sleep(1)
        print("\nBurp")

    # --- ZONA DE PRUEBAS (MAIN) ---
# Aquí es donde usamos el plano para crear vida real.

# Instanciamos (Creamos) a la mascota

r2 = CyberPet("R2-D2_Dark")

# Interactuamos  (usando el punto .)
r2.status()
r2.jugar()
r2.jugar()
r2.status()
r2.alimentar()
r2.status()


bb8 = CyberPet("BB-8_evil")
bb8.jugar()
bb8.jugar()
bb8.status()