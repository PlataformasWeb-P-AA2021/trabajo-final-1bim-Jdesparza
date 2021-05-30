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

print("Los cantones que tiene establecimientos con 0 número de profesores")
establecDocentes = session.query(Canton, Parroquia, Establecimiento)\
    .join(Parroquia, Canton.id == Parroquia.canton_id)\
    .join(Establecimiento, Parroquia.id == Establecimiento.parroquia_id)\
    .filter(Establecimiento.docentes == 0).all()

for e in establecDocentes:
    print(e)
#print(len(establecDocentes))

print("============================================================\n"+
    "============================================================")
print("Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21")
establecParroquia = session.query(Establecimiento, Parroquia)\
    .join(Parroquia, Establecimiento.parroquia_id == Parroquia.id)\
    .filter(Parroquia.nombre == "CATACOCHA", Establecimiento.estudiantes >= 21).all()

for e in establecParroquia:
    print(e)
#print(len(establecParroquia))
