import os 
from getpass import getpass
from tabulate import tabulate
from Conexion import *
import Usuario
import Contrasena

conexion = conectar()
crear_tablas(conexion)

def inicio():
    os.system('cls')
    comprobar = Usuario.comprobar_usuario()
    if len(comprobar) == 0:
        print('Bienvenido, registre su información')
        nombre = input('Ingrese su nombre : ')
        apellido = input('Ingrese su apellido : ')
        contrasena_maestra = getpass('Ingrese su contraseña maestra : ')
        respuesta = Usuario.registrar( nombre, apellido, contrasena_maestra)
        if respuesta == 'Registro correcto':
            print(f'Bienvenido {nombre}')
            menu()
        else:
            print(respuesta)
    else:
        contrasena_maestra = getpass('Ingrese su contraseña maestra: ')
        respuesta = Usuario.comprobar_contrasena(1, contrasena_maestra)
        if len(respuesta) == 0:
            print('Contraseña incorrecta')
        else:
            print('Bienvenido')
            menu()




def menu():
    while True:
        print('------BIENVENIDO-------')
        print('Seleccione una de las siguientes opciones: ')
        print('\t1. Añadir contraseña')
        print('\t2. Ver todas las contraseñas')
        print('\t3. Visualizar una contraseña')
        print('\t4. Modificar contraseña')
        print('\t5. Eliminar contraseña')
        print('\t6. Salir')
        
        opcion = input('Ingrese una opción: ')

        if opcion == '1' :
            nueva_contrasena()
            print(' ')
        elif opcion == '2' :
            print('Visualizando las contraseñas...')
            print(' ')
        elif opcion == '3' :
            print('Visualizando una contraseña...')
            print(' ')
        elif opcion == '4' :
            print('Modificando contraseña...')
            print(' ')
        elif opcion == '5' :
            print('Eliminando contraseña...')
            print(' ')
        elif opcion == '6' :
            break
        else:
            print(' ')
            print('Esta opción no es válida.')
#menu()
def nueva_contrasena():
    nombre = input('Ingrese el nombre: ')
    url = input('Ingrese la url: ')
    nombre_usuario = input('Ingrese el nombre de usuario: ')
    contrasena = input('Ingrese la contraseña: ')
    descripcion = input('Ingrese la descripción: ')
    respuesta = contrasena.registrar(nombre, url, nombre_usuario, contrasena, descripcion)
    print(respuesta)



inicio()
















