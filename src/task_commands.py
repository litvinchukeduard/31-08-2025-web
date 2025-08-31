from abc import ABC, abstractmethod
from dataclasses import dataclass
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


class AllTasksCommand(Command):
    def __init__(self, tasks_list: list[Task]):
        self.tasks_list = tasks_list

    def execute(self):
        if len(self.tasks_list) > 0:
            print("Here are all your tasks:")
            for task in self.tasks_list:
                print(
                    f"(Task id {task.id}) {task.description} [Done: {task.is_completed}]"
                )
        else:
            print("No tasks to display")


@dataclass
class MarkTaskAsDoneCommand(Command):
    task_id: int
    tasks_list: list[Task]

    def execute(self):
        for (
            task
        ) in (
            self.tasks_list
        ):  # OPTIONAL TODO: If we have too many tasks, use a dictionary instead {1: Task(1, "Hello", False)}
            if task.id == self.task_id:
                task.is_completed = True
                return


class ExitCommand(Command):
    def __init__(self, save_strategy, tasks_list):
        self.save_strategy = save_strategy
        self.tasks_list = tasks_list

    def execute(self):
        print("Goodbye!")
        self.save_strategy.save(self.tasks_list)
        exit()
