from datetime import datetime
from typing import List
from organizando_mi_mundo.models.task import Task


class TaskManager:
    """Gestor de tareas: añade, lista y marca tareas como completadas.

    Esta clase centraliza la colección de tareas y las operaciones sobre ellas,
    separando la responsabilidad de `TaskController`.
    """

    def __init__(self):
        self._tasks: List[Task] = []

    def add_task(self, title: str, description: str, due_datetime: datetime, has_time: bool = True) -> Task:
        """Crea una nueva `Task`, la agrega a la lista y la devuelve."""
        task = Task(title, description, due_datetime, has_time)
        self._tasks.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        """Devuelve una copia de la lista de tareas."""
        return list(self._tasks)

    def complete_task(self, index: int) -> Task:
        """Marca la tarea en la posición `index` como completada.

        Lanza `IndexError` si el índice no es válido.
        """
        if index < 0 or index >= len(self._tasks):
            raise IndexError("Índice de tarea inválido")
        self._tasks[index].mark_completed()
        return self._tasks[index]

    def count(self) -> int:
        """Número de tareas gestionadas."""
        return len(self._tasks)
