import imp
from re import T
import sqlite3
from sqlite3 import Error
from .conneccion import create_connect

def new_usuario(data):
    conn = create_connect()
    sql = """ INSERT INTO user (nombre, correo) 
                VALUES(?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print('Nuevo usuario creado')
        return True
    except Error as e:
        print('Error al crear usuario'+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def actualizar(_id,data):
    conn = create_connect()

    sql = f"""UPDATE user SET
                            nombre = ?,
                            correo = ?
        WHERE user_id = {_id}

    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Usuario actualizado")
        return True
    except Error as e:
        print('Error al actualizar usuario'+ str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def eliminar_usuario(_id):
    conn = create_connect()
    sql = f"DELETE FROM user WHERE user_id = {_id}"


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Usuario eliminado")
        return True
    except Error as e:
        print("Error al eliminar usuario:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_nombre(nombre):
    conn = create_connect()
    sql = f"SELECT * FROM user WHERE nombre = '{nombre}'"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        nombrex = cur.fetchall()
        conn.commit()
        return nombrex
    except Error as e:
        print("Error el buscar nombre:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_correo(correo):
    conn = create_connect()
    sql = f"SELECT * FROM user WHERE correo = '{correo}'"
    
    try:
        cur = conn.cursor()
        cur.execute(sql)
        coreex = cur.fetchall()
        conn.commit()
        return coreex
    except Error as e:
        print("Error el curcar correo:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def buscar_id(correo):
    conn = create_connect()
    sql = f"SELECT user_id FROM user WHERE correo = '{correo}'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        coreex = cur.fetchall()
        conn.commit()
        return coreex
    except Error as e:
        print("Error el curcar correo:" + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()