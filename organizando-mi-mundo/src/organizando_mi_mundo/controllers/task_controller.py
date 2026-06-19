"""Controlador principal del proyecto.

Contiene `TaskController`, que orquesta el flujo de la aplicación entre
el modelo (`TaskManager`) y la vista (`TaskView`).

Responsabilidades:
- interpretar la entrada del usuario
- validar entradas básicas
- delegar operaciones al `TaskManager`
- formatear y delegar salidas a la `TaskView`
"""

import pandas as pd
from datetime import datetime

from organizando_mi_mundo.models.task_manager import TaskManager
from organizando_mi_mundo.views.task_view import TaskView


class TaskController:
    """Controlador que maneja la lógica entre el modelo y la vista."""

    def __init__(self):
        self.manager = TaskManager()
        self.view = TaskView(self)

    def run(self):
        """Inicia la aplicación gráfica."""
        self.view.start()

    def add_task(self, title: str, description: str, due_datetime: datetime, has_time: bool):
        """Añade una tarea y actualiza la vista."""
        try:
            self.manager.add_task(title, description, due_datetime, has_time)
            self.view.display_tasks(self.manager.list_tasks())
            self.view.notify("Tarea creada", f"'{title}' se agregó correctamente.")
            self.view.speak(f"Tarea creada: {title}")
        except ValueError as error:
            self.view.show_warning(str(error))
            self.view.speak(str(error))

    def complete_task(self, index: int):
        """Marca la tarea en la posición dada como completada."""
        if self.manager.count() == 0:
            self.view.show_warning("No hay tareas para marcar como completadas.")
            self.view.speak("No hay tareas registradas para completar.")
            return

        try:
            task = self.manager.complete_task(index)
            self.view.display_tasks(self.manager.list_tasks())
            self.view.notify("Tarea completada", "¡Muy bien! La tarea se marcó como completada.")
            self.view.speak(f"Tarea completada: {task.title}")
        except IndexError:
            self.view.show_warning("Número de tarea inválido.")
            self.view.speak("El número de tarea no es válido.")

    def export_tasks(self, filename: str):
        """Exporta las tareas actuales a CSV usando pandas."""
        if self.manager.count() == 0:
            self.view.show_warning("No hay tareas para exportar.")
            self.view.speak("No hay tareas para exportar.")
            return

        data = [
            {
                "Título": task.title,
                "Descripción": task.description,
                "Vencimiento": (
                    task.due_datetime.strftime("%d/%m/%Y %H:%M")
                    if getattr(task, "has_time", True)
                    else task.due_datetime.strftime("%d/%m/%Y")
                ),
                "Completada": task.completed,
            }
            for task in self.manager.list_tasks()
        ]

        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        self.view.show_info(f"Tareas exportadas a '{filename}'.")
        self.view.notify("Exportación completa", f"Archivo guardado en {filename}")
        self.view.speak("Exportación completada. El archivo se guardó correctamente.")

    def parse_due_datetime(self, date_text: str, time_text: str):
        """Convierte fecha y hora en un objeto datetime válido."""
        if not date_text:
            raise ValueError("La fecha es obligatoria.")

        try:
            due_date = datetime.strptime(date_text, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de fecha inválido. Usa dd/mm/aaaa.")

        if time_text:
            try:
                due_time = datetime.strptime(time_text, "%H:%M").time()
            except ValueError:
                raise ValueError("Formato de hora inválido. Usa HH:MM.")
            due_datetime = datetime.combine(due_date, due_time)
            if due_datetime < datetime.now():
                raise ValueError("La fecha y hora deben ser actuales o futuras.")
        else:
            due_time = datetime.min.time()
            due_datetime = datetime.combine(due_date, due_time)
            if due_date < datetime.now().date():
                raise ValueError("La fecha debe ser actual o futura.")

        return due_datetime

    def check_due_tasks(self):
        """Revisa tareas vencidas y notifica cuando llegue la fecha."""
        now = datetime.now()
        due_tasks = []
        for task in self.manager.list_tasks():
            if not task.completed and not task.notified and task.due_datetime <= now:
                self.view.notify("Tarea vencida", f"La tarea '{task.title}' tiene la fecha de vencimiento programada.")
                self.view.speak(f"La tarea {task.title} debe comenzar hoy.")
                task.notified = True
                due_tasks.append(task)
        return due_tasks
