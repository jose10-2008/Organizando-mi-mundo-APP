import pytest
from datetime import datetime, timedelta

from organizando_mi_mundo.models.task import Task


def test_task_creation():
    due_datetime = datetime.now() + timedelta(days=1)
    task = Task("Prueba", "Descripción", due_datetime)
    assert task.title == "Prueba"
    assert task.description == "Descripción"
    assert not task.completed
    assert task.due_datetime == due_datetime


def test_task_creation_without_time():
    due_datetime = datetime.now().date()
    task = Task("Prueba", "Descripción", datetime.combine(due_datetime, datetime.min.time()), has_time=False)
    assert task.title == "Prueba"
    assert task.description == "Descripción"
    assert task.due_datetime.date() == due_datetime
    assert not task.has_time


def test_mark_completed():
    due_datetime = datetime.now() + timedelta(days=1)
    task = Task("Prueba", "Descripción", due_datetime)
    task.mark_completed()
    assert task.completed


def test_task_creation_invalid_title():
    due_datetime = datetime.now() + timedelta(days=1)
    with pytest.raises(ValueError, match="título de la tarea no puede estar vacío"):
        Task("", "Descripción", due_datetime)
