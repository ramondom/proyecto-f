from dal.db import Db

def obtener_id(id):
    sql = '''SELECT id, nombre, capacidad, formato
            FROM Salas 
            WHERE id = ? ;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def existe(nombre):
    sql = "SELECT COUNT(*) FROM Salas WHERE nombre = ?;"
    parametros = (nombre,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def agregar(nombre, capacidad, formato):    
    sql = "INSERT INTO Salas(nombre, capacidad, formato) VALUES(?, ?, ?);"
    parametros = (nombre, capacidad, formato)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT *
            FROM Salas;'''
    result = Db.consultar(sql)
    return result

def actualizar(id, nombre, capacidad, formato):    
    sql = "UPDATE Salas SET nombre = ?, capacidad = ?, formato = ? WHERE id = ?;"
    parametros = (nombre, capacidad, formato, id)
    Db.ejecutar(sql, parametros)   

def eliminar(id):
        sql = "DELETE FROM Salas WHERE id = ?;"
        parametros = (id,)
        Db.ejecutar(sql, parametros)