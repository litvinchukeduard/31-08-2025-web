from src.task_commands import (
    AddTaskCommand,
    ExitCommand,
    AllTasksCommand,
    MarkTaskAsDoneCommand,
)

from src.save_strategies import JsonSaveStrategy
from src.logger import Logger


def main():
    logger = Logger()
    print("Welcome to task manager!")
    logger.log.info("Starting application")
    save_strategy_name = input("Please choose file format (json/csv/pkl): ")
    match save_strategy_name:
        case "json":
            save_strategy = JsonSaveStrategy()
        case "csv":
            # save_strategy = CsvSaveStrategy()
            ...
            return
        case "pkl":
            # save_strategy = PickleSaveStrategy()
            ...
            return

    logger.log.debug(f"Loading files from file. Strategy: {save_strategy_name}")
    task_list = save_strategy.load()

    actions_dict = {
        "add": lambda: AddTaskCommand(
            input("Please enter task description: "), task_list
        ).execute(),
        "all": lambda: AllTasksCommand(task_list).execute(),
        "done": lambda: MarkTaskAsDoneCommand(
            int(input("Enter task id: ")), task_list
        ).execute(),
        "exit": lambda: ExitCommand(save_strategy, task_list).execute(),
    }

    while True:
        action = input("Select action: (add/all/done/exit): ").strip().lower()
        if action in actions_dict:
            actions_dict[action]()


if __name__ == "__main__":
    main()
