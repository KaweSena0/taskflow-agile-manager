from src.task_manager import TaskManager
import pytest

def test_create_task():
    manager = TaskManager()
    task = manager.create_task("Nova tarefa")

    assert task["title"] == "Nova tarefa"

def test_invalid_task():
    manager = TaskManager()

    with pytest.raises(ValueError):
        manager.create_task("")