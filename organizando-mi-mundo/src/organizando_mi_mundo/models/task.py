from datetime import datetime


class Task:
    """Modelo que representa una tarea dentro de Organizando Mi Mundo."""

    def __init__(self, title: str, description: str, due_datetime: datetime, has_time: bool = True):
        """Inicializa una nueva tarea.

        Args:
            title (str): El título o nombre de la tarea.
            description (str): Una descripción breve de la tarea.
            due_datetime (datetime): Fecha y hora de vencimiento.
            has_time (bool): Indica si la hora fue proporcionada.

        Raises:
            ValueError: Si el título está vacío o la fecha no es válida.
        """
        title = title.strip()
        if not title:
            raise ValueError("El título de la tarea no puede estar vacío.")

        if not isinstance(due_datetime, datetime):
            raise ValueError("La fecha de vencimiento debe ser un objeto datetime válido.")

        self.title = title
        self.description = description.strip()
        self.completed = False
        self.due_datetime = due_datetime
        self.has_time = has_time
        self.notified = False

    def mark_completed(self):
        """Marca la tarea como completada."""
        self.completed = True

    def __str__(self):
        """Devuelve una representación en texto de la tarea."""
        estado = "Completada" if self.completed else "Pendiente"
        if self.has_time:
            due = self.due_datetime.strftime("%d/%m/%Y %H:%M")
        else:
            due = self.due_datetime.strftime("%d/%m/%Y")
        return f"{self.title} - {estado}: {self.description} (Vence: {due})"
