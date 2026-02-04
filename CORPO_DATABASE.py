import time

print("---[ARASAKA PERSONNEL DATABASE (LEAKED)]")

#1 L a estructura de datos (JSON Style)
# CLAVE(ID: Valor (Diccionario con detalles)

db_empleados = {
    "VAMP":{
        "nombre": "Inti",
        "rol": "AI & Automation Developer",
        "salario": 23500,
        "nivel_acceso": 4
    },
    "JOHNNY":{
        "nombre": "Johnny Silverhand",
        "rol": "Rockerboy",
        "salario": 50,
        "nivel_acceso": 1
    },
    "GMAN":{
        "nombre": "Uknown",
        "rol": "Interdimensional Bureaucrat",
        "salario": 0,
        "nivel_acceso":10
    }
}

#2 El buscador

while True:
    print(f"\n[SYSTEM] Records available: {len(db_empleados)}")
    query = input("ENTER EMPLOYEE ID (or 'EXIT'): ").upper()

    if query == "EXIT": 
        print("Closing Conection...")
        break

    if query in db_empleados:
        data = db_empleados[query]
        
        print("\n---RECORD FOUND---")
        print(f"NAME: {data['nombre']}")
        print(f"ROLE: {data['rol']}")
        #FOrmato de dinero: ${:,} pone comas de miles
        print(f"SALARY: ${data['salario']:,}MXN")
        print(f"LEVEL: {data['nivel_acceso']}")
        print("-----------------------")

    else:
        print(f"ERROR ID '{query}' not found in database.")
