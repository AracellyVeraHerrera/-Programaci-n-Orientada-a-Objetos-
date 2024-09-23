import tkinter as tk
from tkinter import messagebox

# Funciones
def add_task():
    task = entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.itemconfig(selected_task_index, {'bg': 'lightgrey'})
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea primero.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea primero.")

# Ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Entrada y botones
entry = tk.Entry(root, width=35)
entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.grid(row=0, column=1, padx=10, pady=10)

complete_button = tk.Button(root, text="Marcar Completada", command=complete_task)
complete_button.grid(row=1, column=0, padx=10, pady=10)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.grid(row=1, column=1, padx=10, pady=10)

# Lista de tareas
task_listbox = tk.Listbox(root, height=10, width=50)
task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Atajos de teclado
root.bind('<Return>', lambda event: add_task())
root.bind('<c>', lambda event: complete_task())
root.bind('<Delete>', lambda event: delete_task())
root.bind('<d>', lambda event: delete_task())
root.bind('<Escape>', lambda event: root.quit())

root.mainloop()