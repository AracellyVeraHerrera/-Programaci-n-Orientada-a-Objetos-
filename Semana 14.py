import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la lista de eventos
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10)

        # TreeView para mostrar los eventos
        self.eventos_tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.eventos_tree.heading("Fecha", text="Fecha")
        self.eventos_tree.heading("Hora", text="Hora")
        self.eventos_tree.heading("Descripción", text="Descripción")
        self.eventos_tree.pack()

        # Frame para la entrada de datos
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10)

        # Campos de entrada
        tk.Label(self.frame_entrada, text="Fecha (DD/MM/AAAA):").grid(row=0, column=0)
        self.fecha_entry = tk.Entry(self.frame_entrada)
        self.fecha_entry.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(self.frame_entrada)
        self.desc_entry.grid(row=2, column=1)

        # Botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.btn_salir.grid(row=0, column=2)

    # Función para agregar evento
    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        desc = self.desc_entry.get()
        if fecha and hora and desc:
            self.eventos_tree.insert('', 'end', values=(fecha, hora, desc))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos")

    # Función para eliminar evento
    def eliminar_evento(self):
        selected_item = self.eventos_tree.selection()
        if selected_item:
            self.eventos_tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

    # Función para limpiar campos
    def limpiar_campos(self):
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()