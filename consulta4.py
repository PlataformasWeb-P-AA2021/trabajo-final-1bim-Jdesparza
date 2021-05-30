from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and y or

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Establecimiento

# se importa información del archivo configuracion
from configuracion import cadenaTFinal
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadenaTFinal)


Session = sessionmaker(bind=engine)
session = Session()

print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores")
establecOrden1 = session.query(Establecimiento)\
    .filter(Establecimiento.docentes > 100)\
    .order_by(Establecimiento.estudiantes).all()

for e in establecOrden1:
    print(e)
#print(len(establecOrden1))

print("============================================================\n"+
    "============================================================")
print("Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores")
establecOrden2 = session.query(Establecimiento)\
    .filter(Establecimiento.docentes > 100)\
    .order_by(Establecimiento.docentes).all()

for e in establecOrden2:
    print(e)
#print(len(establecOrden2))