import os


class Colors:
    SEA_BLUE = '\033[38;5;32m'
    OCEAN_BLUE = '\033[38;5;33m'
    SKY_BLUE = '\033[38;5;39m'
    AQUA = '\033[38;5;45m'
    WAVE_BLUE = '\033[38;5;27m'
    WARNING_RED = '\033[38;5;196m'
    ALERT_RED = '\033[38;5;160m'
    DANGER_RED = '\033[38;5;124m'
    EXIT_COLOR = '\033[38;5;208m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


tasks = []
status_dict = {}


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def handle_input():
    while True:
        try:
            return int(
                input(Colors.SEA_BLUE + "Please choose an option by entering the corresponding number: " + Colors.ENDC))
        except ValueError:
            print(Colors.ALERT_RED + "Invalid input. Please enter a number." + Colors.ENDC)


def update_status():
    for task in tasks:
        if task not in status_dict:
            status_dict[task] = 'Uncompleted'
    for task in list(status_dict.keys()):
        if task not in tasks:
            del status_dict[task]


def add_task():
    new_task = input(Colors.SEA_BLUE + "\nEnter your task (or type 0 to return): " + Colors.ENDC).strip()
    if new_task == "0":
        return
    tasks.append(new_task)
    status_dict[new_task] = 'Uncompleted'
    print(Colors.EXIT_COLOR + f"\nTask '{new_task}' added successfully!\n" + Colors.ENDC)


def show_tasks():
    if not tasks:
        print(Colors.SEA_BLUE + "\nNo tasks available." + Colors.ENDC)
        return

    print(Colors.SEA_BLUE + "\n-- Current Tasks --\n" + Colors.ENDC)
    for idx, (task, status) in enumerate(status_dict.items(), 1):
        print(f"{idx}. {task} -- {status}")


def show_filtered_tasks(status_filter):
    filtered_tasks = {task: status for task, status in status_dict.items() if status == status_filter}
    if not filtered_tasks:
        print(Colors.SEA_BLUE + "\nNo matching tasks." + Colors.ENDC)
        return

    for idx, (task, status) in enumerate(filtered_tasks.items(), 1):
        print(f"{idx}. {task} -- {status}")


def change_task_status():
    show_tasks()
    if not tasks:
        return

    while True:
        try:
            task_number = int(
                input(Colors.BOLD + "\nEnter the task number to toggle status (or 0 to return): " + Colors.ENDC))
            if task_number == 0:
                return
            if 1 <= task_number <= len(status_dict):
                selected_task = list(status_dict.keys())[task_number - 1]
                new_status = "Completed" if status_dict[selected_task] == "Uncompleted" else "Uncompleted"
                status_dict[selected_task] = new_status
                print(Colors.SEA_BLUE + f"\nTask '{selected_task}' updated to '{new_status}'." + Colors.ENDC)
                return
            else:
                print(Colors.ALERT_RED + "Invalid task number. Please try again." + Colors.ENDC)
        except ValueError:
            print(Colors.ALERT_RED + "Invalid input. Please enter a valid task number." + Colors.ENDC)


def remove_task():
    show_tasks()
    if not tasks:
        return

    while True:
        try:
            task_number = int(
                input(Colors.DANGER_RED + "\nEnter the task number to remove (or 0 to return): " + Colors.ENDC))
            if task_number == 0:
                return
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                del status_dict[removed_task]
                print(Colors.EXIT_COLOR + f"\nTask '{removed_task}' removed successfully!\n" + Colors.ENDC)
                return
            else:
                print(Colors.ALERT_RED + "Invalid task number. Please try again." + Colors.ENDC)
        except ValueError:
            print(Colors.ALERT_RED + "Invalid input. Please enter a valid number." + Colors.ENDC)


def preview_tasks():
    while True:
        print(Colors.SEA_BLUE + "\nChoose an option:\n" +
              Colors.SKY_BLUE + "1. Show all tasks\n" +
              Colors.OCEAN_BLUE + "2. Show uncompleted tasks\n" +
              Colors.AQUA + "3. Show completed tasks\n" +
              Colors.WAVE_BLUE + "4. Change task status\n" +
              Colors.WARNING_RED + "5. Back to main menu" + Colors.ENDC)

        user_choice = handle_input()
        if user_choice == 1:
            show_tasks()
        elif user_choice == 2:
            show_filtered_tasks("Uncompleted")
        elif user_choice == 3:
            show_filtered_tasks("Completed")
        elif user_choice == 4:
            change_task_status()
        elif user_choice == 5:
            return
        else:
            print(Colors.ALERT_RED + "Invalid input. Please enter a number within the range." + Colors.ENDC)


def main_menu():
    while True:
        print(Colors.SKY_BLUE + "\nTask Manager:\n" +
              Colors.OCEAN_BLUE + "1. Add Task\n" +
              Colors.AQUA + "2. Preview Tasks\n" +
              Colors.WARNING_RED + "3. Remove Task\n" +
              Colors.EXIT_COLOR + "4. Exit" + Colors.ENDC)

        user_choice = handle_input()
        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            preview_tasks()
        elif user_choice == 3:
            remove_task()
        elif user_choice == 4:
            print(Colors.EXIT_COLOR + "\nExiting Task Manager. Goodbye!" + Colors.ENDC)
            break
        else:
            print(Colors.ALERT_RED + "Invalid input. Please enter a valid number." + Colors.ENDC)


if __name__ == "__main__":
    clear_screen()
    main_menu()
