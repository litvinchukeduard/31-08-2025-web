from src.task_entity import Task

task_one = Task(1, "Example", False)
{
    "id": 1,
    "description": "Example",
    "is_completed": False
}
task_dict = {
    "id": task_one.id,
    "description": task_one.description,
    "is_completed": task_one.is_completed
}

# print(task_one)
# print(task_one.__dict__)

# loaded_task = Task(task_dict["id"], task_dict["description"], task_dict["is_completed"])
loaded_task = Task(**task_dict)
print(loaded_task)
