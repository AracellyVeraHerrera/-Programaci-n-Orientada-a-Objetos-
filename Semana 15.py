import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x300")

        # Lista para almacenar las tareas
        self.tasks = []

        # Crear un campo de entrada para añadir nuevas tareas
        self.entry = tk.Entry(self.root, width=35)
        self.entry.grid(row=0, column=0, padx=10, pady=10)

        # Botón para añadir tareas
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Crear una Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, height=10, width=40, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Evento para añadir tarea al presionar Enter
        self.entry.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{task} (Completada)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()