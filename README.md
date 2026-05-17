# Actividad 3 - Bases de Datos

## Descripción del proyecto

Este proyecto fue desarrollado en Python y utiliza MySQL junto con SQLAlchemy y Faker para la generación automática de datos.

El programa se conecta a una base de datos MySQL, crea una tabla automáticamente y genera **100000 registros falsos** para simular información real.

---

## Tecnologías utilizadas

- Python
- MySQL
- SQLAlchemy
- Faker
- python-dotenv

---

## Estructura del proyecto

```
proyecto_faker_bd/
│
├── main.py
├── .env.example
├── .gitignore
└── README.md
```

---

## Ejecución del proyecto

### 1. Instalar dependencias

```bash
pip install sqlalchemy pymysql faker python-dotenv
```

## 2. Ejecutar el proyecto

```bash
python main.py
```

---

##  4. Agregar resultado del proyecto

```md id="extra"
## Resultado

- Se crea la tabla automáticamente
- Se generan 100mil registros falsos
- Se insertan en MySQL usando SQLAlchemy