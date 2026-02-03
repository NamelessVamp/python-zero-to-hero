import time

print("---[PASSWORD CRACKER v1.0]")
target_pin = 7
print(f"TARGET DETECTED. LOCK PIN: ****")
print("INITIATING BRUTE FORCE ATTACK...\n")

#Ciclo FOR
#range (1, 11) genera numeros del 1 al 10
#'intento' es la variable que cambia en cada vuelta (1,2,3,...)

for intento in range (1,11):
    #:04d rellan con ceros a la izquierda (1 -> 0001)
    # end=" " hace que no salte de linea, dando efecto de escaneo
    print(f"[LOG] Testing PIN: {intento:04d}...", end="")
    
    time.sleep(3) # Pausa dramática para simular "procesamiento"

    #LA DESICION DENTRO DEL LOOP
    if intento == target_pin:
        print("Match Found!")
        print(">>>ACCES GRANTED<<<")
        break #<--- COMANDO CRÍTICO: Detiene el ciclo inmediatamente.
    else:
        print("Failed")

print("\n---ATTACK FINISHED---")