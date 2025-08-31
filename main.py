from src.task_commands import AddTaskCommand, ExitCommand

def main():
    print("Welcome to task manage!")

    task_list = []

    actions_dict = {
        "add": lambda: AddTaskCommand(input("Please enter task description: "), task_list).execute(),
        "exit": lambda: ExitCommand().execute()
    }

    while True:
        action = input("Select action: (add/exit): ").strip().lower()
        if action in actions_dict:
            actions_dict[action]()


if __name__ == '__main__':
    main()
