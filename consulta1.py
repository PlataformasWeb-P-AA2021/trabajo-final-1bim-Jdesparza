from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia, Canton, Parroquia, Establecimiento

# se importa información del archivo configuracion
from configuracion import cadenaTFinal
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadenaTFinal)


Session = sessionmaker(bind=engine)
session = Session()

print("Todos los establecimientos de la provincia de Loja")
establecimientosProv = session.query(Establecimiento, Parroquia, Canton, Provincia)\
    .join(Parroquia, Establecimiento.parroquia_id == Parroquia.id)\
    .join(Canton, Parroquia.canton_id == Canton.id).join(Provincia, Canton.provincia_id == Provincia.id)\
    .filter(Provincia.nombre == "LOJA").all()

for e in establecimientosProv:
    print(e)
#print(len(establecimientosProv))

print("============================================================\n"+
    "============================================================")
print("Todos los establecimientos del cantón de Loja")
establecimientosCan = session.query(Establecimiento, Parroquia, Canton).join(Parroquia, Establecimiento.parroquia_id == Parroquia.id)\
    .join(Canton, Parroquia.canton_id == Canton.id)\
    .filter(Canton.nombre == "LOJA").all()

for e in establecimientosCan:
    print(e)
#print(len(establecimientosCan))








