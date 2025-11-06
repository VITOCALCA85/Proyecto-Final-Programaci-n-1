import sqlite3

DB_NAME = "mapas.db"

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute
        
    conn.commit()
    conn.close()

def agregar_mapa(nombre, tipo, año, ubicación, notas):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mapas (nombre, tipo, año, ubicación, notas) VALUES (?, ?, ?, ?, ?)",
                   (nombre, tipo, año, ubicación, notas))
    conn.commit()
    conn.close()

def listar_mapas():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mapas")
    datos = cursor.fetchall()
    conn.close()
    return datos
