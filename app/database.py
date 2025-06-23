import sqlite3
from pathlib import Path

DB_PATH = Path("data/omia_exam_grader.db")

def conectar():
    """Establece una conexión con SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    return conn

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Candidatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            documento TEXT,
            correo_electronico TEXT,
            rol_aplicacion TEXT,
            fecha_aplicacion TEXT,
            puntaje INTEGER,
            aprobado BOOLEAN
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Respuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_candidato INTEGER,
            numero_pregunta INTEGER,
            respuesta_marcada TEXT,
            respuesta_correcta TEXT,
            es_correcta BOOLEAN,
            FOREIGN KEY (id_candidato) REFERENCES Candidatos(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_tablas()
    print("Base de datos creada correctamente en:", DB_PATH)
