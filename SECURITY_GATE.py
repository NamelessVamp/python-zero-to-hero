import time

print("---[Arasaka Decure Gateway v4.0]")

#1 INPUTS
password = input("ENTER PASSWORD: ")
#Convertimos a int de una vez para comparar numeros
nivel = int(input("CLEARENCE LEVEL (1-10): "))

print("\nVerfiying credentials")
time.sleep(1) #Suspenso...

#2. LOGIC CORE (Aqui vive la inteligencia)
#Usamos '==' para comparar si es igual
#Usamos 'and' para exigir DOS condicionales

if password == "VAMP_HACK" and nivel >= 5:
    print("ACCES GRANTED")
    print("Welcome Back")
    print("Protocol: BLACK_OPS initiated")

elif password == "VAMP_HACK" and nivel <5:
    print("ACCES DENIED")
    print(f"Reason: Level {nivel} is too low for this sector.")
    print("Please contact Administrator")

else:
    print("INTRUDER DETECTED")
    print("Tracking IP address...")
    print("Locking terminal in 3... 2...1...")
