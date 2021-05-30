from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia

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
#se obtiene solo el codigo y nombre de la provincia
#Se guarda en la tabla los datos
archivo = open('data/Listado-Instituciones-Educativas.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
lineas = lineas[1:]
lineas = [l.split("|") for l in lineas]
lineas = [(l[2], l[3]) for l in lineas]
provincias = list(set(lineas))

for linea in provincias:
    #print(linea)
    provincia = Provincia(id=linea[0] , nombre=linea[1])
    session.add(provincia)

archivo.close()

# se confirma las transacciones
session.commit()