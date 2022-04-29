# Proyecto Final - Archivos csv [Python]
# Proyecto Final Python Inicial

# Autor: Juan Eduardo Flores
# Version: 1.0

import csv
import os
from unicodedata import normalize



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
        cabecera = ['legajo', 'nomapel', 'materia', 'nota1', 'nota2', 'nota3', 'nota4', 'nota5', 'nota6', 'nota7', 'nota8', 'nota9', 'nota10']
        escritor = csv.DictWriter(notas_alumnos_csv, fieldnames=cabecera)
        escritor.writeheader()
    notas_alumnos_csv.close()

#Crear Archivo csv de Notas
def crear_archivo_notas(archivo):
    if (os.path.isfile(archivo)):
        accion = input("El archivo ya existe, desea eliminarlo y crear uno nuevo? (S/N)?: ")
        if accion.upper() == 'S':
            crea_archivo(archivo)
            print("ARCHIVO CREADO CON EXITO")
    else:
        crea_archivo(archivo)
        print("ARCHIVO CREADO CON EXITO")

# Ingreso de notas
def ingresar_notas():
    notas = []
    nota = 100
    cantidad = 0
    while nota != 0 and cantidad <= 10:
        nota = int(input("Ingrese la nota del alumno, ingrese 0 para finalizar: "))
        if nota >= 1 and nota <= 10:
            notas.append(nota)
            cantidad += 1
        elif nota != 0:
            print("Debe ingresar una nota entre 1 y 10")
    for i in range(cantidad,10):
        notas.append(0)  
    return notas

# antes de agregar un alumno buscamos sis este no existe
def buscar_alumno(archivo, legajo):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            datos = list(csv.DictReader(notas_alumnos_csv))  
        alumno = ""
        for fila in datos:
            if fila['legajo'] == legajo:
                alumno = fila['nomapel']
        return alumno

# Validamos si el alumno tiene notas en la materia
def validar_alumno_materia(archivo,legajo,materia):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            datos = list(csv.DictReader(notas_alumnos_csv))        
        encontrado = False
        for fila in datos:
            if fila['legajo'] == legajo and fila['materia'] == materia.upper():
                encontrado = True
        return encontrado
    
# Agregar Alumnos al archivo de notas csv
def agregar_datos_alumnos(archivo):
    if (os.path.isfile(archivo)):
        #cabecera = ['legajo', 'nomapel', 'materia', 'nota1', 'nota2', 'nota3', 'nota4', 'nota5', 'nota6', 'nota7', 'nota8', 'nota9', 'nota10']
        #with open(archivo, 'a', newline='') as notas_alumnos_csv:
            #escritor = csv.writer(notas_alumnos_csv)
            while True:
                with open(archivo, 'a', newline='') as notas_alumnos_csv:
                    escritor = csv.writer(notas_alumnos_csv)
                    legajo= input("Ingrese el número de legajo: ")
                    nomapel = buscar_alumno(archivo,legajo)
                    if nomapel != "":
                        materia = input("Ingrese el nombre de la materia: ")
                        trans_tab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)
                        materia = normalize('NFKC', normalize('NFKD', materia).translate(trans_tab))
                        if validar_alumno_materia(archivo,legajo,materia):
                            print("El alumno ingresado ya tiene notas en la materia seleccionada")
                        else:
                            notas = ingresar_notas()   
                            alumno = [legajo, nomapel.upper(),materia.upper()] + notas
                            escritor.writerow(alumno)
                    else:    
                        nomapel = input("Ingrese el nombre y apellido del alumno: ")
                        materia = input("Ingrese el nombre de la materia:")
                        notas = ingresar_notas()
                        alumno = [legajo, nomapel.upper(),materia.upper()] + notas
                        escritor.writerow(alumno)
                    elegir = input("Desea agregar un nuevo alumnos? (S/N): ")
                    if elegir.upper() != 'S':
                        break
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
        
#def Impresion de resultados
def evaluar_imprimir(datos,materia):
    suma = 0
    cantidad = 0
    notas = []
    i = 1
    for fila in datos:
        if fila['materia'] == materia.upper():
            vble = 'nota' + str(i)
            while int(fila[vble]) != 0:
                notas.append(fila[vble])
                suma += int(fila[vble])
                cantidad += 1
                i += 1
                vble = 'nota'+str(i)
            promedio = suma / cantidad
        if promedio >= 0 and promedio < 6:
            condicion = 'LIBRE'
        elif promedio >= 6 and promedio < 8:
            condicion = 'REGULAR'
        else:
            condicion = 'PROMOCIÓN'
        print("=" * 80)
        print(fila['nomapel'],"obtuvo las siguientes notas en ",materia.upper(),": ",notas)
        print("La nota final de ",fila['nomapel']," en ",materia.upper()," es ", promedio," y su condicion final es: ",condicion)        
        print("=" * 80)
 
#Impresion de resultados
def evaluar_imprimir_todas(datos,materias):
    for materia in materias:
        suma = 0
        cantidad = 0
        notas = []
        i = 1
    for fila in datos:
        if fila['materia'] == materia.upper():
            vble = 'nota' + str(i)
            while int(fila[vble]) != 0:
                notas.append(fila[vble])
                suma += int(fila[vble])
                cantidad += 1
                i += 1
                vble = 'nota'+str(i)
            promedio = suma / cantidad
        if promedio >= 0 and promedio < 6:
            condicion = 'LIBRE'
        elif promedio >= 6 and promedio < 8:
            condicion = 'REGULAR'
        else:
            condicion = 'PROMOCIÓN'
        print("=" * 80)
        print(fila['nomapel'],"obtuvo las siguientes notas en ",materia.upper(),": ",notas)
        print("La nota final de ",fila['nomapel']," en ",materia.upper()," es ", promedio," y su condicion final es: ",condicion)        
        print("=" * 80)

# Calcular nota y condición final por materia
def nota_condicion_final_materia(archivo):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            datos = list(csv.DictReader(notas_alumnos_csv))       
        materia = input("Materia de la que desea ver la nota y condicion final de los alumnos: ")
        print("=" * 80)   
        evaluar_imprimir(datos,materia.upper())
        notas_alumnos_csv.close()
    else:
        print("El archivo no existe todavía, debe crearlo")
    
# Calcular nota y condición final
def nota_condicion_final(archivo):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            datos = list(csv.DictReader(notas_alumnos_csv))
            datos = sorted(datos, key=lambda d: int(d['legajo']))                   
        materias = materias_en_archivo_csv(datos)      
        print("=" * 80)
        evaluar_imprimir_todas(datos,materias)
        notas_alumnos_csv.close()
    else:
        print("El archivo no existe todavía, debe crearlo")

# Impresión de estadisticas
def impimir_estadisticas(materia,alumnos,aprobados,desaprobados,promocionados,regulares,libres):
    print("=" * 80)
    print("En la materia ",materia," hay ",alumnos,"alumnos")
    print("=" * 80)
    print(aprobados," alumnos aprobaron la materia", materia)
    print(desaprobados," alumnos desaprobaron la materia", materia)   
    print('=' * 80)
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
    print("=" * 80)
    print(promocionados, "alumnos promocionaron la materia ",materia)
    print(regulares,"alumnos regularizaron la materia ",materia)
    print(libres,"alumnos quedaron libres en la materia ",materia)
    print("=" * 80)
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
    
    print("=" * 80)

# Calcular estadisticas por materias
def estadisticas_x_materia(archivo):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            datos = list(csv.DictReader(notas_alumnos_csv))
        materia = input("Materia de la que desea ver la nota y condicion final de los alumnos: ")
        materias = materias_en_archivo_csv(datos)
        if materia in materias:
            aprobados = 0
            desaprobados = 0
            promocionados = 0
            regulares = 0
            libres = 0
            alumnos = 0
            for fila in datos:
                suma = 0
                i = 1
                cantidad = 0
                notas = []
                if fila['materia'] == materia.upper(): 
                    vble = 'nota' + str(i)
                    while int(fila[vble]) != 0:
                        notas.append(fila[vble])
                        suma += int(fila[vble])
                        cantidad += 1
                        i += 1
                        vble = 'nota'+str(i)
                promedio = suma / cantidad
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
        else:
            print("La materia",materia.upper(),"No se encuentra en el archivo")
        notas_alumnos_csv.close()
    else:
        print("El archivo no existe todavía, debe crearlo")

# Calcular estadisticas de todas las materias
def estadisticas(archivo):
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
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
                suma = 0
                i = 1
                cantidad = 0
                notas = []
                if fila['materia'] == materia:     
                    vble = 'nota' + str(i)
                    while int(fila[vble]) != 0:
                        notas.append(fila[vble])
                        suma += int(fila[vble])
                        cantidad += 1
                        i += 1
                        vble = 'nota'+str(i)
                promedio = suma / cantidad
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
    if (os.path.isfile(archivo)):
        with open(archivo) as notas_alumnos_csv:
            datos = list(csv.DictReader(notas_alumnos_csv))
            datos = sorted(datos, key=lambda d: int(d['legajo'])) 
        if len(datos) != 0:
            for fila in datos:
                print("=" * 80)
                suma = 0
                i = 1
                cantidad = 0
                notas = [] 
                vble = 'nota' + str(i)
                while int(fila[vble]) != 0:
                    notas.append(fila[vble])
                    suma += int(fila[vble])
                    cantidad += 1
                    i += 1
                    vble = 'nota'+str(i)
                print(fila['nomapel']," - ",fila['materia']," - NOTAS: ",notas)
        else:
            print('NO HAY ALUMNOS REGISTRADOS EN EL CURSO')

        print("=" * 80)
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