# Trabajo Final Primer Bimestre

### Por:Jordy David Esparza Rivera

## Aspectos importantes del código

En el siguiente trabajo se hizo el uso de SQLite para la creación de la BD y SQLAlchemy para la creación de tablas, la subida de datos a la BD y para realizar las consultas correspondientes.

Primeramente se identifico que datos existen en la ***data***

![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/0.png)

Y una vez analisados se concluyo que existen ***4*** entidades y los datos que corresponden a cada una son:

* Provincia:
	* Código División Política Administrativa Provincia
	* Provincia

	### Creación de tabla Provincia

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/1.png) 

* Canton:
	* Código División Política Administrativa  Cantón
	* Cantón

	### Creación de tabla Canton
	* Aparte de los dos datos de Canton, se agrega el dato provincia_id por la relacion entre tablas

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/2.png) 

* Parroquia:
	* Código División Política Administrativa  Parroquia
	* Parroquia

	### Creación de tabla Parroquia
	* Aparte de los dos datos de Parroquia, se agrega el dato canton_id por la relacion entre tablas

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/3.png)

* Establecimiento
	* Código AMIE
	* Nombre de la Institución Educativa
	* Código de Distrito
	* Sostenimiento
	* Tipo de Educación
	* Tipo de Educación
	* Jornada
	* Acceso (terrestre/ aéreo/fluvial)
	* Número de estudiantes
	* Número de docentes

	### Creación de tabla Establecimiento
	* Aparte de los diez datos de Parroquia, se agrega el dato parroquia_id por la relacion entre tablas

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/4.png)

Por otra parte para el ingreso de los datos en cada entidad creada, primeramente se leyó el archivo ***Listado-Instituciones-Educativas.csv*** y para el ingreso de los datos a la entidad solo se saco del archivo los datos que le corresponden a la entidad y que sean datos unicos, a exepción para las entidades Canton, Parroquia y Establecimiento ya que para ellos también se saco el codigo que corresponde para la relacion de tablas (FK).

A continuación se muestra como se ingreso los datos a cada entidad:

* Provincia:

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/5.png)

* canton:

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/6.png)

* Parroquia:

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/7.png)

* Establecimiento:

	![](https://github.com/PlataformasWeb-P-AA2021/trabajo-final-1bim-Jdesparza/tree/main/img/8.png)

Y ya una vez que se tuvo ingresados los datos a cada tabla se procedio a realizar las consultas especificadas.

## Orden de ejecución de los Archivos

Algo a tener en cuenta antes de ejecutar los archivos, es que existen dos archivos más, el de configuracion.py que es en donde se especifica las conficuraciones para la base de datos (aqui se encuentra como se llamara la BD que se creara en SQLite) y el de analisis_datos.py que es en donde se leyó el archivo con la finalidad de realizar el analisis correspondiente. Por lo tanto no es necesario ejecutar estos dos archivos, ya que no afectan a la creación de tablas o a la subida de datos y en el caso de querer ejecutarlos se recomienda ejecutar el de configuracion.py primeramente y luego sí los demas que se especifican más adelante, y el de analisis_datos.py se puede ejecutar en cualquier momento.

Además cabe recalcar que como no se subio la base de datos ***basetFinal.db** al repositorio hay que ejecutar los archivos de la siguiente forma:

* genera_tablas.py
	* Este archivo es el que se debe ejecutar ***primero***, dado que este es el que contiene la creación de las tablas.

* ingresa_provincias.py
	* Este archivo se ejecuta ***segundo***, dado a que contiene la subida de los datos de la tabla Provincia

* ingresa_cantones.py
	* Este archivo se ejecuta ***tercero***, dado a que contiene la subida de los datos de la tabla Canton

* ingresa_parroquias.py
	* Este archivo se ejecuta ***cuerto***, dado a que contiene la subida de los datos de la tabla Parroquia

* ingresa_establecimientos.py
	* Este archivo se ejecuta ***quito***, dado a que contiene la subida de los datos de la tabla Establecimiento

Con respecto a los archivos de consulta, aqui no importa el orden de ejecución, se puede ejecutar en cualquier orden:

* consulta1.py
* consulta2.py
* consulta3.py
* consulta4.py
* consulta5.py

## Uso de SqlAlchemy

Dada la información de la carpeta ***data***. Realizar las siguientes tareas:

* Analizar el contenido

* Identificar las posibles entidades que se puedan generar

* Las entidades deben satisfacer lo siguiente:
	* Un establecimiento tiene características propias.
	* Un establecimiento pertenece a una parroquia.
	* Una parroquia pertence a un cantón.
	* Un cantón pertence a un provincia.

* Generar un proceso de generación de entidades a través de SqlAlchemy. Usar Sqlite
	* genera_tablas.py

* Ingresar la información en cada entidad creada.
	* ingresa_provincias.py
	* ingresa_cantones.py
	* ingresa_parroquias.py
	* ingresa_establecimientos.py

* Generar las siguientes consultas:
	* consulta1.py
		* Todos los establecimientos de la provincia de Loja.
		* Todos los establecimientos del cantón de Loja.
	* consulta2.py
    	* Las parroquias que tienen establecimientos únicamente en la jornada Nocturna
		* Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459
	* consulta3.py
		* Los cantones que tiene establecimientos con 0 número de profesores
		* Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21
	* consulta4.py
		* Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores. 
		* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.
	* consulta5.py
		* Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.
		* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.
