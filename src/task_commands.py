from abc import ABC, abstractmethod
# from dataclasses import dataclass
from sys import exit

from src.task_entity import Task


current_id = 0


class Command(ABC):
    @abstractmethod
    def execute(self): ...


"""
Add task

add-task

"Do the dishes"
"""

# tasks = []


class AddTaskCommand(Command):
    def __init__(self, description: str, task_list: list[Task]):
        self.description = description
        self.task_list = task_list

    def execute(self):
        global current_id
        current_id += 1
        new_task = Task(current_id, self.description, False)
        self.task_list.append(new_task)



class ExitCommand(Command):
    def execute(self):
        print("Goodbye!")
        exit()
