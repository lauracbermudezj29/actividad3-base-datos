import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date, insert
from sqlalchemy.orm import declarative_base
from faker import Faker


def main():

    # 1. Cargar variables de entorno
    load_dotenv()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    # 2. Conexión a MySQL
    engine = create_engine(
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    )

    try:
        conn = engine.connect()
        print("✅ Conexión exitosa a MySQL")
    except Exception as e:
        print("Error de conexión:", e)
        return

    # 3. Definir tabla
    Base = declarative_base()

    class Persona(Base):
        __tablename__ = "personas_laura"

        id = Column(Integer, primary_key=True, autoincrement=True)
        nombre = Column(String(50))
        apellido = Column(String(50))
        telefono = Column(String(30))
        email = Column(String(100))
        fecha_nacimiento = Column(Date)
        empresa = Column(String(100))

    # 4. Creamos la tabla en la base de datos
    Base.metadata.create_all(engine)
    print("✅ Tabla creada exitosamente")

    # 5. Generar datos con Faker (lista de diccionarios)
    fake = Faker()

    data = []

    for _ in range(100000):
        data.append({
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "telefono": fake.phone_number(),
            "email": fake.email(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "empresa": fake.company()
        })

    print("✅ Datos generados con Faker")

    # 6. Inserción por lotes, masivamente 
    
    conn.execute(insert(Persona), data)
    conn.commit()

    print("✅ 100000 registros insertados exitosamente")


# 7. Ejecución correcta
if __name__ == "__main__":
    main()