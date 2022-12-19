from dal.db import Db

def obtener_id(id):
    sql = '''SELECT f.id, f.fecha, f.hora, p.id, s.id
            FROM Funciones f
            INNER JOIN Peliculas p ON p.id = f.peliculaId
            INNER JOIN Salas s ON s.id = f.salaId
            WHERE f.id = ?;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def existe(fec, hor, tit, sala):
    sql ='''SELECT f.id, f.fecha, f.hora, p.id, s.id
            FROM Funciones f
            INNER JOIN Peliculas p ON p.id = f.peliculaId
            INNER JOIN Salas s ON s.id = f.salaId
            WHERE f.fecha = ? AND f.hora = ? AND p.id = ? AND s.id = ?;'''
    parametros = (fec, hor, tit, sala)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def agregar(fecha, hora, pel, sala):    
    sql = "INSERT INTO Funciones(fecha, hora, peliculaId, salaId) VALUES(?, ?, ?, ?);"
    parametros = (fecha, hora, pel, sala)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT f.id, f.fecha, f.hora, p.titulo Titulo, s.nombre Sala
            FROM Funciones f
            INNER JOIN Peliculas p ON p.id = f.peliculaId
            INNER JOIN Salas s ON s.id = f.salaId;'''
    result = Db.consultar(sql)
    return result

def listarP():
    sql = "SELECT id, titulo FROM Peliculas ORDER BY 1;"
    result = Db.consultar(sql)
    return result

def listarS():
    sql = "SELECT id, nombre FROM Salas ORDER BY 1;"
    result = Db.consultar(sql)
    return result

def actualizar(id, fecha, hora, pel, sala):    
    sql = "UPDATE Funciones SET fecha = ?, hora = ?, peliculaId = ?, salaId = ? WHERE id = ? ;"
    parametros = (fecha, hora, pel, sala, id)
    Db.ejecutar(sql, parametros)

def eliminar(id):    
    sql = "DELETE FROM Funciones WHERE id = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)
