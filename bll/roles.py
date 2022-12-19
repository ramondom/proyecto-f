from dal.db import Db

def listar():
    sql = "SELECT id, nombre FROM Roles ORDER BY id;"
    result = Db.consultar(sql)
    return result