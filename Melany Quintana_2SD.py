#UNIVERSIDAD AGRARIA DEL ECUADOR
#CARRERA: CIENCIAS DE LA COMPUTACIÓN – MODALIDAD EN LINEA
#Estudiante: Melany Quintana Bedor
#2/12/2025
#Práctica Del Exámen
"""1) Pedir la cantidad de estudiantes (n > 0). Luego, mediante un for, solicitar por cada estudiante: 
- Nombre (str)
- Calificación numérica (float entre 0 y 100)
2) Validar entradas: si la calificación está fuera de rango, mostrar
mensaje y pedirla de nuevo (usar while interno). 
3) Al finalizar, calcular y mostrar: (
- Promedio general (float)
- Nota máxima y mínima con los nombres correspondientes
- Conteo de aprobados (>= 60) y reprobados (< 60)
"""
# Pedimos la cantidad de estudiantes
n = int(input("Ingrese la cantidad de estudiantes (n > 0): ")) 

while n <= 0:   # Validamos que n sea mayor a 0
    print("Error: la cantidad debe ser mayor que 0.")  # Mensaje de error
    n = int(input("Ingrese la cantidad de estudiantes (n > 0): "))  # Se pide de nuevo
 
suma_calificaciones = 0  # Inicia la suma para luego calcular el promedio
max_nota = -1    # Inicia la nota máxima con un valor muy bajo
min_nota = 9999  # Inicializamos la nota mínima con un valor muy alto

# Variables para guardar los nombres
nombre_max = ""   # Nota máxima
nombre_min = ""   # Nota mínima 

aprobados = 0   # Contador de aprobados 
reprobados = 0  # Contador de reprobados

# Ciclo for para procesar cada estudiante
for i in range(n):   
    print(f"\nEstudiante {i + 1}:")  # Indicador del número de estudiante

    nombre = input("Nombre: ") # Pedimos el nombre
    nota = float(input("Calificación (0 - 100): "))  # Pedimos la calificación

    # Validamos la nota 
    while nota < 0 or nota > 100:  # Mientras la nota esté fuera del rango permitido
        print("Error: la calificación debe estar entre 0 y 100.")  # Mostramos mensaje de error
        nota = float(input("Ingrese nuevamente la calificación: ")) # Pedimos otra vez la nota 

    # Sumar nota
    suma_calificaciones += nota   # Acumulamos la calificación para calcular el promedio después

    # Máxima
    if nota > max_nota:   # Verificamos si esta nota es la nueva nota máxima
        max_nota = nota   # Actualizamos la nota máxima
        nombre_max = nombre  # Guardamos el nombre del estudiante con la calificación máxima
        
    # Mínima
    if nota < min_nota:      # Verificamos si esta nota es la nueva nota mínima
        min_nota = nota      # Actualizamos la nota mínima
        nombre_min = nombre  # Guardamos el nombre del estudiante con la calificación mínima

    # Aprobados / Reprobados
    if nota >=60:     # Si la nota es mayor o igual a 60, el estudiante aprueba
        aprobados +=1 # Incrementamos el contador de aprobados
    else:                # Si la nota es menor a 60, el estudiante reprueba
        reprobados +=1  # Incrementamos el contador de reprobados
        
# Calculamos el promedio
promedio = suma_calificaciones / n  # Calculamos el promedio general dividiendo la suma de notas entre la cantidad de estudiantes

# Resultados finales
print("\n----- RESULTADOS GENERALES DE LOS ESTUDIANTES -----")
print(f"Promedio general: {promedio:.2f}")                      # Muestra el promedio   
print(f"Nota máxima: {max_nota} (Estudiante: {nombre_max})")    # Muestra nota máxima y el nombre del estudiante
print(f"Nota mínima: {min_nota} (Estudiante: {nombre_min})")    # Muestra nota mínima y el nombre del estudiante
print(f"Aprobados: {aprobados}")                                # Número de aprobados
print(f"Reprobados: {reprobados}")                              # Número de reprobados
