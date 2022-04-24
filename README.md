# Proyecto Estadística de Alumnos con csv
**_Proyecto Integrador_** - _Python Inicial_

![estadísticas](/images/estadisticas.png)


En este proyecto trabajamos con una planilla CSV en la cual tenemos los siguientes datos correspondientes a alumnos: número de legajo, nombre y apellido del alumno, nombre de la materia que curso y 5 notas que obtuvo en dicha materia (las notas van del 1 al 10), tal como vemos en la imagen siguiente:

 ![csvalumnos](/images/csvalumnos.PNG)
 
Este pequeño aplicativo cuenta con un menú con las siguientes opciones:
 
![menu](/images/opciones.PNG)

El aplicativo analiza los datos contenidos en el archivo CSV y se muestran los resultados solicitados en la terminal.
La opción 1 nos permite determinar si sobreescribimos un archivo existente o bien si deseamos crear un archivo nuevo.
La opción 2 nos permite agregar al archivo existente nuevos datos de alumnos, materia y las notas obtenidas en la misma
La opción 3 nos permite calcular la nota final (promedio de las 5 notas) en cada materia y nos informa la condición final del alumno en dicha materia según el siguiente criterio:
-	Si nota es menor a 6 => La condición será LIBRE
-	Si nota es mayor o igual a 6 y menor que 8 => La condición será REGULAR
-	Si nota es mayor o igual a 8 menor o igual a 10 => La condición será PROMOCIONADO

La opción 4 nos permite calcular la nota final (promedio de las 5 notas) en la materia seleccionada y nos informa la condición final del alumno en dicha materia siguiendo el criterio anteriormente mencionado.
La opción 5 nos permite determinar las estadísticas de cursado de la materia seleccionada; por ejemplo:
	Cantidad total de alumnos que cursaron la materia
*	Cantidad de aprobados y desaprobados
*	Porcentaje de aprobados y desaprobados
*	Porcentaje de alumnos que tienen la condición de LIBRE
*	Porcentaje de alumnos que tienen la condición de REGULAR
*	Porcentaje de alumnos que tienen la condición de PROMOCIONADOS

La opción 6 nos permite determinar las mismas estadísticas de cursado de la opción anterior, pero en este caso de todas las materias contenidas en el CSV

La opción 7 nos permite ver los datos de cada alumno y las notas obtenidas en cada una de las materias contenidas en el archivo CSV.


## Construido con 🛠️

_Para la creación del presente proyecto utilizamos:_

* [Python](https://www.python.org)


## Versión 📌

Versión 1.0

## Autor ✒️

* **Juan Eduardo Flores** - *Trabajo Integrador* - [jefsalta](https://github.com/jefsalta) - e-mail: juaneflores@gmail.com




