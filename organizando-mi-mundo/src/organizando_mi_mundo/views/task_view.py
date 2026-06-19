import threading
import tkinter as tk
from tkinter import filedialog, messagebox

import customtkinter as ctk
from plyer import notification
import pyttsx3


class TaskView:
    """Vista gráfica de tareas usando CustomTkinter."""

    def __init__(self, controller):
        self.controller = controller
        self.speaker = None
        self._speech_lock = threading.Lock()
        try:
            self.speaker = pyttsx3.init()
            self.speaker.setProperty("rate", 170)
            self.speaker.setProperty("volume", 0.9)
        except Exception:
            self.speaker = None

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Organizando Mi Mundo")
        self.root.geometry("760x520")
        self.root.resizable(False, False)

        self._create_widgets()
        self.display_tasks(self.controller.manager.list_tasks())
        self._schedule_due_check()

    def _create_widgets(self):
        header = ctk.CTkLabel(self.root, text="Organizando Mi Mundo", font=ctk.CTkFont(size=24, weight="bold"))
        header.pack(pady=(20, 10))

        form_frame = ctk.CTkFrame(self.root)
        form_frame.pack(fill="x", padx=20, pady=(0, 10))

        self.title_entry = ctk.CTkEntry(form_frame, placeholder_text="Título de la tarea")
        self.title_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10), pady=5)

        self.description_entry = ctk.CTkEntry(form_frame, placeholder_text="Descripción de la tarea")
        self.description_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=5)

        self.date_entry = ctk.CTkEntry(form_frame, placeholder_text="Fecha obligatoria (dd/mm/aaaa)")
        self.date_entry.grid(row=2, column=0, sticky="ew", padx=(0, 10), pady=5)

        self.time_entry = ctk.CTkEntry(form_frame, placeholder_text="Hora opcional (HH:MM)")
        self.time_entry.grid(row=3, column=0, sticky="ew", padx=(0, 10), pady=5)

        form_frame.grid_columnconfigure(0, weight=1)

        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(fill="x", padx=20, pady=(0, 10))

        create_button = ctk.CTkButton(button_frame, text="Agregar tarea", command=self.create_task_command)
        create_button.grid(row=0, column=0, padx=5, pady=5)

        complete_button = ctk.CTkButton(button_frame, text="Marcar completada", command=self.complete_task_command)
        complete_button.grid(row=0, column=1, padx=5, pady=5)

        export_button = ctk.CTkButton(button_frame, text="Exportar a CSV", command=self.export_tasks_command)
        export_button.grid(row=0, column=2, padx=5, pady=5)

        self.task_listbox = tk.Listbox(
            self.root,
            font=("Segoe UI", 11),
            activestyle="none",
            selectbackground="#3B82F6",
            selectforeground="white",
            highlightthickness=1,
            relief="solid",
        )
        self.task_listbox.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        self.status_label = ctk.CTkLabel(self.root, text="Selecciona una tarea y presiona 'Marcar completada'.")
        self.status_label.pack(pady=(0, 10))

    def start(self):
        self.root.mainloop()

    def display_tasks(self, tasks):
        self.task_listbox.delete(0, tk.END)
        if not tasks:
            self.task_listbox.insert(tk.END, "No hay tareas registradas.")
            return

        for index, task in enumerate(tasks, start=1):
            estado = "✅" if task.completed else "❌"
            if getattr(task, "has_time", True):
                due = task.due_datetime.strftime("%d/%m/%Y %H:%M")
            else:
                due = task.due_datetime.strftime("%d/%m/%Y")
            self.task_listbox.insert(tk.END, f"{index}. {estado} {task.title} ({due}) - {task.description}")

    def show_info(self, message):
        messagebox.showinfo("Organizando Mi Mundo", message)

    def show_warning(self, message):
        messagebox.showwarning("Organizando Mi Mundo", message)

    def speak(self, text):
        try:
            self.speaker.say(text)
            self.speaker.runAndWait()
        except Exception:
            pass

    def notify(self, title, message):
        try:
            notification.notify(title=title, message=message, app_name="Organizando Mi Mundo", timeout=3)
        except Exception:
            pass

    def _schedule_due_check(self):
        self.check_due_tasks()
        self.root.after(60000, self._schedule_due_check)

    def check_due_tasks(self):
        self.controller.check_due_tasks()

    def create_task_command(self):
        title = self.title_entry.get().strip()
        description = self.description_entry.get().strip()
        date_text = self.date_entry.get().strip()
        time_text = self.time_entry.get().strip()

        if not title:
            self.show_warning("El título no puede estar vacío.")
            self.speak("El título no puede estar vacío.")
            return

        has_time = bool(time_text)
        try:
            due_datetime = self.controller.parse_due_datetime(date_text, time_text)
        except ValueError as error:
            self.show_warning(str(error))
            self.speak(str(error))
            return

        self.controller.add_task(title, description, due_datetime, has_time)
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

    def complete_task_command(self):
        selection = self.task_listbox.curselection()
        if not selection:
            self.show_warning("Selecciona una tarea para marcarla como completada.")
            self.speak("Por favor, selecciona una tarea antes de marcarla como completada.")
            return

        index = selection[0]
        self.controller.complete_task(index)

    def export_tasks_command(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="tareas.csv",
            title="Guardar tareas como",
        )
        if not filename:
            return

        self.controller.export_tasks(filename)
        self.speak("Las tareas se exportaron correctamente.")
