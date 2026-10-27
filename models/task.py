class Task:
    """Модель задачи."""
    def __init__(self, task_id, title):
        if not title:
            raise ValueError("Название не может быть пустым")
        self.id = task_id
        self.title = title

class Database:
    """Простая база данных в памяти."""
    def __init__(self):
        self.tasks = []
        self.counter = 1

    def save(self, title):
        task = Task(self.counter, title)
        self.tasks.append(task)
        self.counter += 1
        return task

    def get_all(self):
        return self.tasks
