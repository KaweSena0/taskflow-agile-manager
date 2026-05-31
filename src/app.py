from task_manager import TaskManager

manager = TaskManager()

manager.create_task("Criar sistema")
manager.create_task("Implementar testes")

print(manager.list_tasks())