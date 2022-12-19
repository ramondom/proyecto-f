from dal.db import Db

def agregar(apellido, nombre, fecha_nacimiento, dni, correo_electronico, usuario, contrasenia, rol_Id):    
    sql = "INSERT INTO Usuarios(apellido, nombre, fechaNacimiento, dni, mail, usuario, contraseña, rolId) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, usuario, Db.encriptar_contraseña(contrasenia), rol_Id)
    Db.ejecutar(sql, parametros)

def actualizar(id, apellido, nombre, fecha_nacimiento, dni, correo_electronico, contrasenia, rol_Id):    
    sql = "UPDATE Usuarios SET apellido = ?, nombre = ?, fechaNacimiento = ?, dni = ?, mail = ?, contraseña = ?, rolId = ? WHERE id = ? AND activo = 1;"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, Db.encriptar_contraseña(contrasenia), rol_Id, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Usuarios SET activo = 0 WHERE id = ? AND activo = 1;"
    else:
        sql = "DELETE FROM Usuarios WHERE id = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT u.id, u.apellido, u.nombre, u.fechaNacimiento, u.dni, u.mail, u.usuario, u.rolId, r.nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.rolId = r.id
            WHERE u.activo = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(usuario):    
    sql = '''SELECT u.id, u.apellido, u.nombre, u.fechaNacimiento, u.dni, u.mail, u.usuario, u.rolId, r.nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.rolId = r.id
            WHERE u.usuario LIKE ? AND u.activo = 1;'''    
    parametros = ('%{}%'.format(usuario),)    
    result = Db.consultar(sql, parametros)
    return result

def validar(usuario, contrasenia):    
    sql = "SELECT usuario FROM Usuarios WHERE usuario = ? AND contraseña = ? AND activo = 1;"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)
    return result != None

def existe(usuario):
    sql = "SELECT COUNT(*) FROM Usuarios WHERE usuario = ? AND activo = 1;"
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def obtener_id(id):
    sql = '''SELECT u.id, u.apellido, u.nombre, u.fechaNacimiento, u.dni, u.mail, u.usuario, u.rolId, r.nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.RolId = r.id
            WHERE u.id = ? AND u.Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def obtener_nombre_usuario(usuario):
    sql = '''SELECT u.id, u.apellido, u.nombre, u.fechaNacimiento, u.dni, u.mail, u.usuario, u.rolId, r.nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.rolId = r.id
            WHERE u.usuario = ? AND u.activo = 1;'''
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)    
    return result