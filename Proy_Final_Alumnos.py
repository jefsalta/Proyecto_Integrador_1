# Proyecto Final - Archivos csv [Python]
# Proyecto Final Python Inicial

# Autor: Juan Eduardo Flores
# Version: 1.0

import csv
import os

# ---------INICIO DE LAS FUNCIONES--------------------- 
# Menu de opciones
def menu():
    print("------------ OPCIONES ------------")
    print("1.- Crear Archivo de alumnos y notas")
    print("2.- Agregar alumnos y notas")
    print("3.- Calcular Nota y Condición Final de todas las materias")
    print("4.- Calcular Nota y Condición Final por materia")
    print("5.- Estadísticas de rendimiento por materia")
    print("6.- Estadisticas de rendimiento de todas las materias")
    print("7.- Mostrar contenido del archivo")
    print("0.- Finalizar")
    try:
        eleccion = int(input(" Seleccione una opción: "))
        return eleccion
    except:
        pass
    

#Crea Archivo csv
def crea_archivo(archivo):
    with open(archivo, 'w', newline='') as notas_alumnos_csv:
        # Columnas
        cabecera = ['legajo', 'nomapel', 'materia', 'nota1', 'nota2','nota3','nota4','nota5']
        # Crear el objeto para escribir las lineas de archivo 
        escritor = csv.DictWriter(notas_alumnos_csv, fieldnames=cabecera)
        escritor.writeheader()
    notas_alumnos_csv.close()

#Crear Archivo csv de Notas
def crear_archivo_notas(archivo):
    # Abrir archivo para escritura
    if (os.path.isfile(archivo)):
        accion = input("El archivo ya existe, desea eliminarlo y crear uno nuevo? (S/N)?: ")
        if accion.upper() == 'S':
            crea_archivo(archivo)
            print("ARCHIVO CREADO CON EXITO")
    else:
        crea_archivo(archivo)
        print("ARCHIVO CREADO CON EXITO")


# Agregar Alumnos al archivo de notas csv
def agregar_datos_alumnos(archivo):
    #verificamos si el archivo existe
    if (os.path.isfile(archivo)):
        # Especificamos los valores del header (cabecera)
        cabecera = ['legajo', 'nomapel', 'materia', 'nota1', 'nota2', 'nota3', 'nota4','nota5']
        # Abrimos el archivo CSV de notas para agregar el nomapel de los alumnos (atributo "a")
        with open(archivo, 'a', newline='') as notas_alumnos_csv:
            # Generar un "escritor" para modificar el archivo
            escritor = csv.DictWriter(notas_alumnos_csv, fieldnames=cabecera)

            while True:
                # Agregar un nuevo alumno
                legajo= input("Ingrese el número de legajo: ")
                nomapel = input("Ingrese el nombre y apellido del alumno: ")
                materia = input("Ingrese el nombre de la materia:")
                nota1 = input("Ingrese la 1er nota del alumno (1-10): ")
                nota2 = input("Ingrese la 2da nota del alumno(1-10): ")
                nota3 = input("Ingrese la 3er nota del alumno(1-10): ")
                nota4 = input("Ingrese la 4ta nota del alumno(1-10): ")
                nota5 = input("Ingrese la 5ta nota del alumno(1-10): ")
                nuevo_alumno = {'legajo': legajo,'nomapel': nomapel.upper(), 'materia': materia.upper(), 'nota1': nota1, 'nota2': nota2, 'nota3': nota3, 'nota4': nota4, 'nota5': nota5}

                # Escribimos los datos del alumno en el archivo
                escritor.writerow(nuevo_alumno)
                elegir = input("Desea agregar un nuevo alumnos? (S/N): ")
                if elegir.upper() != 'S':
                    break
            
        # Cerrar el archivo
        notas_alumnos_csv.close()
    else:
        print("El archivo todavía no existe, debe crearlo")
    
# Armo la lista de materias contenidas en el archivo CSV
def materias_en_archivo_csv(datos):
    materias = []
    for fila in datos:
        if fila['materia'] not in materias:
            materias.append(fila['materia'])
    return materias


        
def evaluar_imprimir(nombre,promedio,materia,nota1,nota2,nota3,nota4,nota5):
    if promedio >= 0 and promedio < 6:
        condicion = 'LIBRE'
    elif promedio >= 6 and promedio < 8:
        condicion = 'REGULAR'
    else:
        condicion = 'PROMOCIÓN'
    
    print("=" * 80)
    print(nombre,"obtuvo las siguientes notas en ",materia.upper(),": ",nota1,'-',nota2,'-',nota3,'-',nota4,'-',nota5)
    print("La nota final de ",nombre," en ",materia.upper()," es ", promedio," y su condicion final es: ",condicion)        
    print("=" * 80)
        
# Calcular nota y condición final por materia
def nota_condicion_final_materia(archivo):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            # Leer todos los datos y almacenarlos en una lista de diccionarios
            datos = list(csv.DictReader(notas_alumnos_csv))
        
        materia = input("Materia de la que desea ver la nota y condicion final de los alumnos: ")
        print("=" * 70)
    
        suma = 0
        for fila in datos:
            if fila['materia'] == materia.upper():
                suma = int(fila['nota1']) + int(fila['nota2']) + int(fila['nota3']) + int(fila['nota4']) + int(fila['nota5'])
                promedio = suma / 5

                evaluar_imprimir(fila['nomapel'],promedio,materia,fila['nota1'],fila['nota2'],fila['nota3'],fila['nota4'],fila['nota5'])

        notas_alumnos_csv.close()
    else:
        print("El archivo no existe todavía, debe crearlo")
    
    
# Calcular nota y condición final
def nota_condicion_final(archivo):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            # Leer todos los datos y almacenarlos en una lista de diccionarios
            datos = list(csv.DictReader(notas_alumnos_csv))
            # Ordena lista de diccionarios por legajo para que aparezcan todas las materias juntas
            datos = sorted(datos, key=lambda d: int(d['legajo'])) 
                    
        materias = materias_en_archivo_csv(datos)
        
        print("=" * 80)
        for materia in materias:
            suma = 0
            for fila in datos:
                if fila['materia'] == materia:
                    suma = int(fila['nota1']) + int(fila['nota2']) + int(fila['nota3']) + int(fila['nota4']) + int(fila['nota5'])
                    promedio = suma / 5
                    
                    evaluar_imprimir(fila['nomapel'],promedio,materia,fila['nota1'],fila['nota2'],fila['nota3'],fila['nota4'],fila['nota5'])
                    
        notas_alumnos_csv.close()
    else:
        print("El archivo no existe todavía, debe crearlo")


# Impresión de estadisticas
def impimir_estadisticas(materia,alumnos,aprobados,desaprobados,promocionados,regulares,libres):
    print("=" * 70)
    print("En la materia ",materia," hay ",alumnos,"alumnos")
    print("=" * 70)
    print(aprobados," alumnos aprobaron la materia", materia)
    print(desaprobados," alumnos desaprobaron la materia", materia)   
    print('=' * 70)
    if aprobados != 0:
        porc_aprobados = (aprobados * 100) / alumnos
        print("Porcentaje de alumnos aprobados en",materia,":",round(porc_aprobados,2),"%")
    else:
        print("Porcentaje de alumnos aprobados en",materia,": 0 %")
    if desaprobados != 0:
        porc_desaprobados = (desaprobados * 100) / alumnos
        print("Porcentaje de alumnos desaprobados en ",materia,":",round(porc_desaprobados,2),"%")
    else:
        print("Porcentaje de alumnos desaprobados en",materia," 0 %")
    print("=" * 70)
    print(promocionados, "alumnos promocionaron la materia ",materia)
    print(regulares,"alumnos regularizaron la materia ",materia)
    print(libres,"alumnos quedaron libres en la materia ",materia)
    print("=" * 70)
    if promocionados != 0:
        porc_promocionados = (promocionados * 100) / alumnos
        print("Porcentaje de alumnos promocionados en ",materia,":",round(porc_promocionados,2),"%")
    else:
        print("Porcentaje de alumnos promocionados en", materia," 0 %")
    if regulares != 0:
        porc_regulares = (regulares * 100) / alumnos
        print("Porcentaje de alumnos regulares en ",materia,":",round(porc_regulares,2),"%")
    else:
        print("Porcentaje de alumnos regulares en ",materia,"0 %")
    if libres != 0:
        porc_libres = (libres * 100) / alumnos
        print("Porcentaje de alumnos libres en ",materia,":",round(porc_libres,2),"%")
    else:
        print("Porcentaje de alumnos libres en ",materia,": 0 %")
    
    print("=" * 70)


# Calcular estadisticas por materias
def estadisticas_x_materia(archivo):
    if (os.path.isfile(archivo)):
        # Abrir un archivo CSV usando with open
        with open(archivo) as notas_alumnos_csv:
            # Leer todos los datos y almacenarlos en una lista de diccionarios
            datos = list(csv.DictReader(notas_alumnos_csv))
            
        materia = input("Materia de la que desea ver la nota y condicion final de los alumnos: ")
        archsalida = "condicion_alumnos_"+materia+".csv"
        aprobados = 0
        desaprobados = 0
        promocionados = 0
        regulares = 0
        libres = 0
        alumnos = 0
        
        for fila in datos:
            if fila['materia'] == materia.upper(): 
                suma = int(fila['nota1']) + int(fila['nota2']) + int(fila['nota3']) + int(fila['nota4']) + int(fila['nota5'])
                promedio = suma / 5

                if promedio >= 0 and promedio < 6:
                    libres += 1
                    desaprobados += 1
                elif promedio >= 6 and promedio < 8:
                    regulares += 1
                    aprobados += 1
                else:
                    promocionados += 1
                    aprobados += 1
                
                alumnos += 1
        impimir_estadisticas(materia.upper(),alumnos,aprobados,desaprobados,promocionados,regulares,libres)    
        notas_alumnos_csv.close()
    else:
        print("El archivo no existe todavía, debe crearlo")

# Calcular estadisticas de todas las materias
def estadisticas(archivo):
    if (os.path.isfile(archivo)):
        # Abrir un archivo CSV usando with open
        with open(archivo) as notas_alumnos_csv:
            # Leer todos los datos y almacenarlos en una lista de diccionarios
            datos = list(csv.DictReader(notas_alumnos_csv))

        materias = materias_en_archivo_csv(datos) 
        
        for materia in materias:
            aprobados = 0
            desaprobados = 0
            promocionados = 0
            regulares = 0
            libres = 0
            alumnos = 0
            
            for fila in datos:
                if fila['materia'] == materia: 
                    suma = int(fila['nota1']) + int(fila['nota2']) + int(fila['nota3']) + int(fila['nota4']) + int(fila['nota5'])
                    promedio = suma / 5

                    if promedio >= 0 and promedio < 6:
                        libres += 1
                        desaprobados += 1
                    elif promedio >= 6 and promedio < 8:
                        regulares += 1
                        aprobados += 1
                    else:
                        promocionados += 1
                        aprobados += 1
                    
                    alumnos += 1
            
            impimir_estadisticas(materia,alumnos,aprobados,desaprobados,promocionados,regulares,libres)
                        
        notas_alumnos_csv.close()
    else:

        print("El archivo no existe todavía, debe crearlo")

    
# Función para Leer el archivo csv
def leer_archivo_notas(archivo):
    #Verificar si existe el archivo
    if (os.path.isfile(archivo)):
        # Abrir un archivo CSV usando with open
        with open(archivo) as notas_alumnos_csv:
            # Leer los datos y almacenarlos en una  lista de diccionarios
            datos = list(csv.DictReader(notas_alumnos_csv))
            #ordenados la lista de diccionarios por legajo de alumno
            datos = sorted(datos, key=lambda d: int(d['legajo'])) 

        if len(datos) != 0:
            for fila in datos:
                print("=" * 70)
                print(fila['nomapel']," - ",fila['materia']," - NOTAS: ",fila['nota1'],'-',fila['nota2'],'-',fila['nota3'],'-',fila['nota4'],'-',fila['nota5'])
        else:
            print('NO HAY ALUMNOS REGISTRADOS EN EL CURSO')

        print("=" * 70)
    else:
        print("El archivo no existe todavia, debe crearlo")

def principal():
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            crear_archivo_notas(archivo)
        elif opcion == 2:
            agregar_datos_alumnos(archivo)
        elif opcion == 3:
            nota_condicion_final(archivo)
        elif opcion == 4:
            nota_condicion_final_materia(archivo)
        elif opcion == 5:
            estadisticas_x_materia(archivo)
        elif opcion == 6:
            estadisticas(archivo)
        elif opcion == 7:
            leer_archivo_notas(archivo)
        else:
            print("VALOR FUERA DE RANGO")
        opcion = menu()

#-----------PROGRAMA PRINCIPAL ---------------------

if __name__ == '__main__':
    archivo = "notas_alumnos_final.csv"
    principal()