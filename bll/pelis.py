from dal.db import Db

def listar():
    sql = '''SELECT *
            FROM Peliculas;'''
    result = Db.consultar(sql)
    return result

def eliminar(id):    
    sql = "DELETE FROM Peliculas WHERE id = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def existe(titulo):
    sql = "SELECT COUNT(*) FROM Peliculas WHERE titulo = ? ;"
    parametros = (titulo,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def agregar(tit, desc, gen, act, durac):    
    sql = "INSERT INTO Peliculas(titulo, descripcion, genero, actores, duracion) VALUES(?, ?, ?, ?, ?);"
    parametros = (tit, desc, gen, act, durac)
    Db.ejecutar(sql, parametros)

def actualizar(id, tit, desc, gen, act, durac):    
    sql = "UPDATE Peliculas SET titulo = ?, descripcion = ?, genero = ?, actores = ?, duracion = ? WHERE id = ?;"
    parametros = (tit, desc, gen, act, durac, id)
    Db.ejecutar(sql, parametros)

def obtener_id(id):
    sql = '''SELECT titulo, descripcion, genero, actores, duracion
            FROM Peliculas
            WHERE id = ?;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result
