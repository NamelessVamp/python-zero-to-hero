import VAMP_UTILS

#Usamos las herramientas
VAMP_UTILS.efecto_typing("Iniciando prueba de herramientas...", 0.1)

dado= VAMP_UTILS.tirar_dado(20)
print(f"Goplpe Critico: {dado}")

pass_segura = VAMP_UTILS.generar_password(12)
print(f"Nueva contraseña generada: {pass_segura}")