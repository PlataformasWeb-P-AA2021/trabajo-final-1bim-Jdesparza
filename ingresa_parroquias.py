from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton, Parroquia

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
#se obtiene el codigo de la parroquia, nombre de la parroquia y el 
#codigo del canton para relacionar las tablas a traves de una consulta
#Se guarda en la tabla los datos
archivo = open('data/Listado-Instituciones-Educativas.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
lineas = lineas[1:]
lineas = [l.split("|") for l in lineas]
#se sacan los datos de la entidad y el codigo del canton para la relacion entre tablas
lineas = [(l[4], l[6], l[7]) for l in lineas]
parroquias = list(set(lineas)) #datos Unicos

for linea in parroquias:
    #print(linea)

    consultaCanton = session.query(Canton).filter_by(id=linea[0]).one()
    #print(consultaCanton)

    parroquia = Parroquia(id=linea[1] , nombre=linea[2], cantones=consultaCanton)
    session.add(parroquia)

archivo.close()

# se confirma las transacciones
session.commit()