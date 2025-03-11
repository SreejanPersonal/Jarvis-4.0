# jarvis/tasks/task_manager.py
# Task management
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        self.tasks.append(task_description)

    def list_tasks(self):
        return self.tasks
