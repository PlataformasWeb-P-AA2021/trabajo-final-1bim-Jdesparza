from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Parroquia, Establecimiento

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
#se obtiene todos los datos relacionados con los establecimientos y el 
#codigo de la parroquia para relacionar las tablas a traves de una consulta
#Se guarda en la tabla los datos
archivo = open('data/Listado-Instituciones-Educativas.csv', 'r', encoding='utf-8')
lineas = archivo.readlines()
lineas = lineas[1:]
lineas = [l.split("|") for l in lineas]
lineas = [(l[6], l[0], l[1], l[8], l[9], l[10], l[11], l[12], l[13], l[14], l[15]) for l in lineas]
establecimientos = list(set(lineas))

for linea in establecimientos:
    #print(linea)

    consultaParroquia = session.query(Parroquia).filter_by(id=linea[0]).one()
    #print(consultaParroquia)

    establecimiento = Establecimiento(id=linea[1], nombre=linea[2], distrito=linea[3], sostenimiento=linea[4], 
        tipo=linea[5], modalidad=linea[6], jornada=linea[7], acceso=linea[8], estudiantes=linea[9], 
        docentes=linea[10], parroquias=consultaParroquia)
    session.add(establecimiento)

archivo.close()

# se confirma las transacciones
session.commit()
