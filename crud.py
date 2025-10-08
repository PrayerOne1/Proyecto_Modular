import tkinter as tk
from tkinter import messagebox

# Diccionario para almacenar los datos
datos = {}

# Funciones CRUD
def crear():
    cedula = entry_cedula.get()
    if cedula in datos:
        messagebox.showwarning("Error", "Ya existe un registro con esa cédula.")
        return
    
    datos[cedula] = {
        "nombre": entry_nombre.get(),
        "apellido_paterno": entry_apellido_p.get(),
        "apellido_materno": entry_apellido_m.get(),
        "correo": entry_correo.get(),
        "contraseña": entry_contra.get()
    }
    messagebox.showinfo("Éxito", "Registro creado exitosamente.")
    limpiar_campos()

def editar():
    cedula = entry_cedula.get()
    if cedula not in datos:
        messagebox.showerror("Error", "No existe un registro con esa cédula.")
        return
    
    datos[cedula] = {
        "nombre": entry_nombre.get(),
        "apellido_paterno": entry_apellido_p.get(),
        "apellido_materno": entry_apellido_m.get(),
        "correo": entry_correo.get(),
        "contraseña": entry_contra.get()
    }
    messagebox.showinfo("Éxito", "Registro editado correctamente.")
    limpiar_campos()

def eliminar():
    cedula = entry_cedula.get()
    if cedula in datos:
        del datos[cedula]
        messagebox.showinfo("Éxito", "Registro eliminado.")
        limpiar_campos()
    else:
        messagebox.showerror("Error", "No se encontró un registro con esa cédula.")

def guardar():
    cedula = entry_cedula.get()
    if cedula in datos:
        info = datos[cedula]
        messagebox.showinfo("Información del usuario",
                            f"Cédula: {cedula}\n"
                            f"Nombre: {info['nombre']}\n"
                            f"Apellido Paterno: {info['apellido_paterno']}\n"
                            f"Apellido Materno: {info['apellido_materno']}\n"
                            f"Correo: {info['correo']}\n"
                            f"Contraseña: {info['contraseña']}")
    else:
        messagebox.showerror("Error", "No existe un registro con esa cédula.")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellido_p.delete(0, tk.END)
    entry_apellido_m.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_contra.delete(0, tk.END)
    entry_cedula.delete(0, tk.END)

# Ventana principal
root = tk.Tk()
root.title("CRUD con Tkinter y Diccionario")
root.geometry("400x400")
root.resizable(False, False)

# Etiquetas y entradas
tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Apellido Paterno:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_apellido_p = tk.Entry(root)
entry_apellido_p.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Apellido Materno:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_apellido_m = tk.Entry(root)
entry_apellido_m.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Correo:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_correo = tk.Entry(root)
entry_correo.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Contraseña:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_contra = tk.Entry(root, show="*")
entry_contra.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Cédula:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
entry_cedula = tk.Entry(root)
entry_cedula.grid(row=5, column=1, padx=10, pady=5)

# Botones CRUD
tk.Button(root, text="Crear", bg="#4CAF50", fg="white", command=crear).grid(row=6, column=0, padx=10, pady=15)
tk.Button(root, text="Editar", bg="#2196F3", fg="white", command=editar).grid(row=6, column=1, padx=10, pady=15)
tk.Button(root, text="Eliminar", bg="#F44336", fg="white", command=eliminar).grid(row=7, column=0, padx=10, pady=5)
tk.Button(root, text="Guardar", bg="#FF9800", fg="white", command=guardar).grid(row=7, column=1, padx=10, pady=5)

root.mainloop()
