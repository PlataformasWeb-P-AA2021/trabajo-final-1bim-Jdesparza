from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton

# se importa información del archivo configuracion
from configuracion import cadenaTFinal
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadenaTFinal)

Session = sessionmaker(bind=engine)
session = Session()

#Se lee el archivo .csv y se separa por '|' las columnas
#se obtiene el codigo del canton, nombre del canton y el 
#codigo de la provincia para relacionar las tablas a traves de una consulta
#Se guarda en la tabla los datos
archivo = open('data/Listado-Instituciones-Educativas.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
lineas = lineas[1:]
lineas = [l.split("|") for l in lineas]
lineas = [(l[2], l[4], l[5]) for l in lineas]
cantones = list(set(lineas))

for linea in cantones:
    #print(linea)

    consultaProvincia = session.query(Provincia).filter_by(id=linea[0]).one()
    #print(consultaProvincia)

    canton = Canton(id=linea[1] , nombre=linea[2], provincias=consultaProvincia)
    session.add(canton)

archivo.close()

# se confirma las transacciones
session.commit()