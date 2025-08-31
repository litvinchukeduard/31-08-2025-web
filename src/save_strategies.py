from abc import ABC, abstractmethod
import json
import os.path

from src.task_entity import Task


class SaveStrategy(ABC):
    @abstractmethod
    def save(self, task_list: list[Task]): ...
    
    @abstractmethod
    def load(self) -> list[Task]: ...


class JsonSaveStrategy(SaveStrategy):
    FILE_PATH = "tasks.json"

    def save(self, task_list: list[Task]):
        # task_dict_list = []
        # for task in task_list:
        #     task_dict_list.append(task.__dict__)
        task_dict_list = [task.__dict__ for task in task_list]
        with open(JsonSaveStrategy.FILE_PATH, 'w') as file:
            json.dump(task_dict_list, file)

    def load(self) -> list[Task]:
        if not os.path.isfile(JsonSaveStrategy.FILE_PATH):
            return []
        with open(JsonSaveStrategy.FILE_PATH, 'r') as file:
            task_dict_list = json.load(file)
            return [Task(**task_dict) for task_dict in task_dict_list]
