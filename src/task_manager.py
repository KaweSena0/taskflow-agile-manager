class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title):
        if not title:
            raise ValueError("Título inválido")

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "status": "To Do"
        }

        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks