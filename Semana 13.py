import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entry_dato.get()
    if dato:
        listbox_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un dato.")

# Función para limpiar la lista
def limpiar_datos():
    listbox_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")

# Crear widgets
label_dato = tk.Label(ventana, text="Ingrese datos:")
label_dato.pack(pady=10)

entry_dato = tk.Entry(ventana, width=40)
entry_dato.pack(pady=5)


btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
btn_agregar.pack(pady=5)

listbox_datos = tk.Listbox(ventana, width=50, height=10)
listbox_datos.pack(pady=10)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
btn_limpiar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()