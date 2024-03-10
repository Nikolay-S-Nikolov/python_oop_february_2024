from typing import List

from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:

        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str) -> str:

        try:
            completed_task = next(filter(lambda t: t.name == task_name, self.tasks))

        except StopIteration:
            return f"Could not find task with the name {task_name}"

        completed_task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        cleared_tasks = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                cleared_tasks += 1
        return f"Cleared {cleared_tasks} tasks."

    def view_section(self) -> str:
        result = f'Section {self.name}:\n'
        result += '\n'.join(t.details() for t in self.tasks)
        return result
