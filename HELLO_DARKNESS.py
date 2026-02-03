import time

#1. Simulacion de carga (Bio-Reading)
print("[SYSTEM_BOOT] Initialazing V.A.M.P Protocol...")
time.sleep(2)

print(">>>> CONNECTING TO NEURAL LINK...")
time.sleep(2)

print(">>>> BYPASSING FTEC FIREWALLS...")
time.sleep(1.5)

#2. La Revelacion (Variables)
usuario = "V4MP"
version = "3.14.2"
estado = "ONLINE"

#3. El Output Final (Variables)
#La 'F' antes de las comillas nos deja meter variblaes dentro del texto con {}

print("-" * 30)
print(f"Identity Confirmed: {usuario}")
print(f"Python Kernel: {version}")
print(f"SYSTEM STATUS: {estado}")
print("-"*30)

print("Welcome back, Samurai. We have a city to burn")