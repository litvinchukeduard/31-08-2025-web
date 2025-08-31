from src.task_commands import (
    AddTaskCommand,
    ExitCommand,
    AllTasksCommand,
    MarkTaskAsDoneCommand,
)


def main():
    print("Welcome to task manage!")

    task_list = []

    actions_dict = {
        "add": lambda: AddTaskCommand(
            input("Please enter task description: "), task_list
        ).execute(),
        "all": lambda: AllTasksCommand(task_list).execute(),
        "done": lambda: MarkTaskAsDoneCommand(
            int(input("Enter task id: ")), task_list
        ).execute(),
        "exit": lambda: ExitCommand().execute(),
    }

    while True:
        action = input("Select action: (add/all/done/exit): ").strip().lower()
        if action in actions_dict:
            actions_dict[action]()


if __name__ == "__main__":
    main()
