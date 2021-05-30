from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and y or

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia

# se importa información del archivo configuracion
from configuracion import cadenaTFinal
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadenaTFinal)


Session = sessionmaker(bind=engine)
session = Session()

print("Los establecimientos ordenados por nombre de parroquia "+
    "que tengan más de 20 profesores y la cadena Permanente en tipo de educación")
establecParroquia = session.query(Establecimiento, Parroquia)\
    .join(Parroquia, Establecimiento.parroquia_id == Parroquia.id)\
    .filter(Establecimiento.docentes > 20, Establecimiento.tipo.like("%Permanente%"))\
    .order_by(Parroquia.nombre).all()

for e in establecParroquia:
    print(e)
#print(len(establecParroquia))

print("============================================================\n"+
    "============================================================")
print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02")
establecOrden = session.query(Establecimiento)\
    .filter(Establecimiento.distrito == "11D02")\
    .order_by(Establecimiento.sostenimiento).all()

for e in establecOrden:
    print(e)
#print(len(establecOrden))