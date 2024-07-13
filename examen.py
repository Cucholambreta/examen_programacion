import random
import numpy as np
import csv
import statistics


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos han sido asignados aleatoriamente.")

def clasificar_sueldos():
    menores_800k = []
    entre_800k_y_2M = []
    mayores_2M = []
    
    for i, sueldo in enumerate(sueldos):
        if sueldo < 800000:
            menores_800k.append((trabajadores[i], sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_y_2M.append((trabajadores[i], sueldo))
        else:
            mayores_2M.append((trabajadores[i], sueldo))
    
    print("Clasificación de sueldos:")
    print("1. Sueldos menores a $800.000:")
    print(f"   Trabajador    Sueldo")
    for trabajador, sueldo in menores_800k:
        print(f"   {trabajador}: {sueldo}")
    print(f"   Total: {len(menores_800k)}")
    
    print("2. Sueldos entre $800.000 y $2.000.000:")
    print(f"   Trabajador    Sueldo")
    for trabajador, sueldo in entre_800k_y_2M: 
        print(f"   {trabajador}: {sueldo}")
    print(f"   Total: {len(entre_800k_y_2M)}")
    
    print("3. Sueldos superiores a $2.000.000:")
    print(f"   Trabajador    Sueldo")
    for trabajador, sueldo in mayores_2M:
        print(f"   {trabajador}: {sueldo}")
    print(f"   Total: {len(mayores_2M)}")
    
    total_sueldos = sum(sueldos)
    print(f"Total de sueldos a pagar: ${total_sueldos:,} pesos")

def ver_estadisticas():
    if not sueldos:
        print("No hay sueldos asignados.")
        return
    
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)
    
    print("Estadísticas de sueldos:")
    print(f"Sueldo más alto: {sueldo_mas_alto}")
    print(f"Sueldo más bajo: {sueldo_mas_bajo}")
    print(f"Promedio de sueldos: {promedio_sueldos}")
    print(f"Media geométrica: {media_geometrica}")

def reporte_sueldos():
    if not sueldos:
        print("No hay sueldos asignados.")
        return
    
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Trabajador", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for i, sueldo in enumerate(sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajadores[i], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    
    print("Reporte de sueldos generado en 'reporte_sueldos.csv'.")


while True:
    print("\nMenú:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
        
    opcion = input("Seleccione una opción: ")
        
    if opcion == "1":
        asignar_sueldos_aleatorios()
    elif opcion == "2":
            clasificar_sueldos()
    elif opcion == "3":
        ver_estadisticas()
    elif opcion == "4":
        reporte_sueldos()
    elif opcion == "5":
        print("Finalizando programa...")
        print("Desarrollado por: Alejandro Placencia")
        print("Rut 17.070.619-6")
        break
    else:
        print("Opción no válida. Intente nuevamente.")