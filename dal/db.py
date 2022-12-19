import sqlite3
from datetime import date
import hashlib

database = "cine.db" 

class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                                "id"	INTEGER NOT NULL,
                                "apellido"	TEXT,
                                "nombre"	TEXT,
                                "fechaNacimiento"	TEXT,
                                "dni"	INTEGER,
                                "mail"	TEXT,
                                "usuario"	TEXT UNIQUE,
                                "contraseña"	TEXT,
                                "rolId"	INTEGER,
                                "activo"	INTEGER NOT NULL DEFAULT 1,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );'''

        sql_butacas = '''CREATE TABLE IF NOT EXISTS "Butacas" (
	                        "id"	INTEGER NOT NULL,
	                        "fila"	INTEGER,
	                        "numero"	INTEGER,
                            "disponible"  TEXT DEFAULT "si",
	                        "salaId"	INTEGER,
	                        PRIMARY KEY("id" AUTOINCREMENT)
                        );'''

        sql_descuentos = '''CREATE TABLE IF NOT EXISTS "Descuentos" (
	                            "id"	INTEGER NOT NULL,
	                            "dia"	TEXT,
	                            "tasa"	REAL,
	                            PRIMARY KEY("id" AUTOINCREMENT)
                            );'''

        sql_funciones = '''CREATE TABLE IF NOT EXISTS "Funciones" (
                                "id"	INTEGER NOT NULL,
                                "fecha"	TEXT,
                                "salaId"	INTEGER,
                                "peliculaId"	INTEGER,
                                "hora"	TEXT,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );'''

        sql_peliculas = '''CREATE TABLE IF NOT EXISTS "Peliculas" (
                                "id"	INTEGER NOT NULL,
                                "titulo"	TEXT NOT NULL,
                                "descripcion"	TEXT,
                                "genero"	TEXT,
                                "actores"	TEXT,
                                "duracion"	TEXT,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );'''

        sql_reservas = '''CREATE TABLE IF NOT EXISTS "Reservas" (
                            "id"	INTEGER NOT NULL,
                            "funcionId"	INTEGER,
                            "usuarioId"	INTEGER,
                            "fecha"	TEXT,
                            "precio"	REAL DEFAULT 0,
                            "butacaId"	INTEGER,
                            "descuentoId" INTEGER,
                            PRIMARY KEY("id" AUTOINCREMENT)
                        );'''
                    
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "id"	INTEGER NOT NULL,
                            "nombre"	TEXT NOT NULL UNIQUE,
                            "activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("id")
                        );'''
                
        sql_salas = '''CREATE TABLE IF NOT EXISTS "Salas" (
                            "id"	INTEGER NOT NULL,
                            "nombre"	TEXT,
                            "capacidad"	INTEGER DEFAULT 0,
                            "formato"	TEXT,
                            PRIMARY KEY("id" AUTOINCREMENT)
                        );'''
        
        tablas = {"Usuarios": sql_usuarios, "Butacas": sql_butacas, "Descuentos": sql_descuentos, "Funciones": sql_funciones, "Peliculas": sql_peliculas, "Reservas": sql_reservas, "Roles": sql_roles, "Salas": sql_salas}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles(id, nombre) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Cliente");'''

        sql_descuentos = '''INSERT INTO Descuentos(dia, tasa) 
                    VALUES 
                        ("Lunes", 0.2),
                        ("Martes", 0.15),
                        ("Miercoles", 0.2),
                        ("Jueves", 0.15),
                        ("Viernes", 0.1),
                        ("Sabado", 0.1),
                        ("Domingo", 0.1);'''

        tablas = {"Roles": sql_roles, "Descuentos": sql_descuentos}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()