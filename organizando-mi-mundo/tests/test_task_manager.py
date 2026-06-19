from datetime import datetime, timedelta

from organizando_mi_mundo.models.task_manager import TaskManager


def test_add_and_list_tasks():
    manager = TaskManager()
    due_datetime = datetime.now() + timedelta(days=1)
    manager.add_task("T1", "D1", due_datetime)
    manager.add_task("T2", "D2", due_datetime)
    tasks = manager.list_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "T1"


def test_complete_task():
    manager = TaskManager()
    due_datetime = datetime.now() + timedelta(days=1)
    manager.add_task("T1", "D1", due_datetime)
    manager.complete_task(0)
    tasks = manager.list_tasks()
    assert tasks[0].completed
