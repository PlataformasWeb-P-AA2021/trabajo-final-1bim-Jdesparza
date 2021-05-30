from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_  # se importa el operador and y or

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton, Parroquia, Establecimiento

# se importa información del archivo configuracion
from configuracion import cadenaTFinal
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadenaTFinal)


Session = sessionmaker(bind=engine)
session = Session()

print("Las parroquias que tienen establecimientos únicamente en la jornada Nocturna")
establecimientosNoc = session.query(Parroquia, Establecimiento).join(Establecimiento, Parroquia.id == Establecimiento.parroquia_id)\
    .filter(Establecimiento.jornada == "Nocturna").all()

for e in establecimientosNoc:
    print(e)
#print(len(establecimientosNoc))

print("============================================================\n"+
    "============================================================")
print("Los cantones que tiene establecimientos con número de estudiantes tales como: 448, 450, 451, 454, 458, 459")
establecEstudiantes = session.query(Canton, Parroquia, Establecimiento).join(Parroquia, Canton.id == Parroquia.canton_id)\
    .join(Establecimiento, Parroquia.id == Establecimiento.parroquia_id)\
    .filter(or_(Establecimiento.estudiantes == 448, Establecimiento.estudiantes == 450, 
        Establecimiento.estudiantes == 451, Establecimiento.estudiantes == 454, Establecimiento.estudiantes == 458, Establecimiento.estudiantes == 459)).all()

for e in establecEstudiantes:
    print(e)
#print(len(establecEstudiantes))

