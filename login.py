import tkinter as tk
from tkinter import messagebox
import hashlib
import os
import re

#   Generamos usuario y password temporal (Para eliminar despues)
user_predeter = "correo@correo.com"
pwd_secreto = "Passw0rd123"
    
     #   Funcion para hashear passwords...

def init_hash(new_pwd):

     #   Generamos hasheo con numero de bytes deseados
    output = os.urandom(64)
    hash_gen = hashlib.pbkdf2_hmac(
    'sha256', # <- Protocolo de encriptacion
    new_pwd.encode('utf-8'),
    output,
    1000000
    ).hex()

    #   Hasheo exitoso
    return {'hash': hash_gen, 'sal': output.hex()}

Almacen_tmp = {
    user_predeter: init_hash(pwd_secreto)
}

def validar_correo(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def validar_hashing():

    #   Obtenemos inputs  
    email_input = email.get() 
    pwd_input = pwd.get() 

    if len(email_input) == 0 or len(pwd_input) == 0:
        messagebox.showerror("Error de login", "Llene los campos con la infomacion requerida")


    if not validar_correo(email_input):
        messagebox.showerror("Error de login", "El formato de correo no es valido")
        return

    if email_input not in Almacen_tmp:
        messagebox.showerror("Error al iniciar sesion", "Correo o password incorrectos")
        return

 
    #   Almacenamos los datos obtenidos y su hasheo
    datos_alm = Almacen_tmp[email_input] # Buscamos por el email
    sal_alm = bytes.fromhex(datos_alm['sal'])
    hash_alm = datos_alm['hash']

    
    hash_gen = hashlib.pbkdf2_hmac(
        'sha256', # <- Protocolo de encriptacion
        pwd_input.encode('utf-8'),
        sal_alm,     
        1000000
    ).hex()

    #   Verificamos que coincidan los hasheos
    if hash_gen == hash_alm:
        messagebox.showinfo("Login exitoso", f'Bienvenido, {email_input} Login exitoso')
    else:
        messagebox.showerror("Error al iniciar sesion", "Correo o password incorrectos")

#   Logica del front end:

root = tk.Tk()
root.title("Login")
root.geometry("300x420")

tk.Label(root, text="Correo").pack(pady=10)
email = tk.Entry(root)
email.pack(pady=15)

tk.Label(root, text="Contraseña").pack(pady=20)
pwd = tk.Entry(root, show='*')
pwd.pack(pady= 25)

tk.Button(root, text="Login", command = validar_hashing).pack(pady=30)
tk.Button(root, text="Cancel", command = root.destroy).pack(pady=30)

root.mainloop()