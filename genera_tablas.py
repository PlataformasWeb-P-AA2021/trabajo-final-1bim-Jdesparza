from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadenaTFinal

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadenaTFinal)

Base = declarative_base()

#Se crea la Tabla de Provincias
class Provincia(Base):
    __tablename__ = 'provincia'
    id = Column(Integer, primary_key=True) #Código División Política Administrativa Provincia
    nombre = Column(String(100), nullable=False) #Provincia

    cantones = relationship("Canton", back_populates="provincias")

    
    def __repr__(self):
        return "Provincia: nombre=%s" % (
            self.nombre)

#Se crea la tabla de cantones y cada canton pertenece a una provincia
class Canton(Base):
    __tablename__ = 'canton'
    id = Column(Integer, primary_key=True) #Código División Política Administrativa  Cantón
    nombre = Column(String(100), nullable=False) #Cantón
    provincia_id = Column(Integer, ForeignKey('provincia.id'))

    provincias = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="cantones")
    
    def __repr__(self):
        return "Canton: %s" % (
            self.nombre)

#Se crea la tabla Parroquia y cada parroquia pertenece a un canton
class Parroquia(Base):
    __tablename__ = 'parroquia'
    id = Column(Integer, primary_key=True) #Código División Política Administrativa  Parroquia
    nombre = Column(String(100), nullable=False) #Parroquia
    canton_id = Column(Integer, ForeignKey('canton.id'))

    cantones  = relationship("Canton", back_populates="parroquias")
    establecimientos  = relationship("Establecimiento", back_populates="parroquias")
    
    def __repr__(self):
        return "Parroquia: %s" % (
            self.nombre)

#Se crea la tabla Establecimiento y cada establecimiento pertenece a una parroquia
class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    id = Column(String(8), primary_key=True) #Código AMIE
    nombre = Column(String(100), nullable=False) #Nombre de la Institución Educativa
    distrito = Column(String(100), nullable=False) #Código de Distrito
    sostenimiento = Column(String(100), nullable=False) #Sostenimiento
    tipo = Column(String(100), nullable=False) #Tipo de Educación
    modalidad = Column(String(100), nullable=False) #Modalidad
    jornada = Column(String(100), nullable=False) #Jornada
    acceso = Column(String(100), nullable=False) #Acceso (terrestre/ aéreo/fluvial)
    estudiantes = Column(Integer, nullable=False) #Número de estudiantes
    docentes = Column(Integer, nullable=False) #Número de docentes
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))

    parroquias  = relationship("Parroquia", back_populates="establecimientos")
    
    def __repr__(self):
        return "Establecimiento: %s distrito=%s sostenimiento=%s tipo=%s modalidad=%s jornada=%s acceso=%s "\
        "estudiantes=%s docentes=%s" % (
            self.nombre,
            self.distrito,
            self.sostenimiento,
            self.tipo,
            self.modalidad,
            self.jornada,
            self.acceso,
            self.estudiantes,
            self.docentes)

Base.metadata.create_all(engine)
