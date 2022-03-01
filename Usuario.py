import hashlib
from Conexion import *

def comprobar_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    sentencia_sql = 'SELECT * FROM usuario'
    cursor.execute(sentencia_sql)
    usuario_encontrado = cursor.fetchall()
    conexion.close()
    return usuario_encontrado

def registrar(nombre, apellido, contrasena_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sentencia_sql = '''INSERT INTO usuario
        (nombre, apellido, contrasena_maestra)
        VALUES (?, ?, ?)'''
        cm_cifrada = hashlib.sha256(contrasena_maestra.encode('utf-8')).hexdigest()
        datos = (nombre, apellido, cm_cifrada)
        cursor.execute(sentencia_sql, datos) 
        conexion.commit()
        conexion.close()
        return 'Registro Correcto'

    except Error as err:
        print('Ha ocurrido un error en: ' + ' ' +str(err))


print(registrar('Alexis', 'Acevedo', '12345'))
print(comprobar_usuario())


