class colors:
    # Blue
    SEA_BLUE = '\033[38;5;32m'
    OCEAN_BLUE = '\033[38;5;33m'
    SKY_BLUE = '\033[38;5;39m'
    AQUA = '\033[38;5;45m'
    WAVE_BLUE = '\033[38;5;27m'

    #  Red
    WARNING_RED = '\033[38;5;196m'
    ALERT_RED = '\033[38;5;160m'
    DANGER_RED = '\033[38;5;124m'
    EXIT_COLOR = '\033[38;5;208m'

    ENDC = '\033[0m'  # Reset
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


tasks = []
status_dict = {}


def handle_input():
    while True:
        try:
            usrin = int(
                input(colors.SEA_BLUE + "Please choose an option by entering the corresponding number: " + colors.ENDC))
        except ValueError:
            print(colors.ALERT_RED + "Invalid input. Please enter a number from the list." + colors.ENDC)
        except IndexError:
            print(colors.ALERT_RED + "Invalid input. Please enter a number from the list." + colors.ENDC)
        return usrin


def mapping():
    for task in tasks:
        if task in status_dict.values():
            continue
        status_dict[task] = 'Uncompleted'
    for i in list(status_dict.keys()):
        if i not in tasks:
            status_dict.pop(i)
def add_task():
    try:
        new_task = input(
            colors.SEA_BLUE + "\nEnter your task below. Type 0 to return to the previous menu \n >> " + colors.ENDC)
        if new_task == str(0):
            my_app()
    except ValueError:
        print(colors.ALERT_RED + "Invalid input. Please enter a number." + colors.ENDC)
    tasks.append(new_task)
    print(colors.EXIT_COLOR + f"\nGreat! Your task " + colors.BOLD + f"'{new_task}'" + colors.ENDC + colors.EXIT_COLOR + "is now added.\n" + colors.ENDC)

def preview():
    userinput = int(input(
        colors.SEA_BLUE + "\nPlease choose an option:\n" + colors.SKY_BLUE + "1. Show all tasks\n" + colors.OCEAN_BLUE + "2. Show uncompleted tasks\n" + colors.AQUA + "3. Show completed tasks\n" + colors.WAVE_BLUE + "4. Change task status \n" + colors.WARNING_RED + f"5. Back to main menu{colors.ENDC}\n>> " + colors.ENDC))
    if userinput == 1:
        if len(tasks) == 0:
            print(colors.SEA_BLUE + "no tasks yet" + colors.ENDC)
        else:
            print(colors.SEA_BLUE + "\n-- Current Tasks --\n" + colors.ENDC)
            for idx, (task, status) in enumerate(status_dict.items(), 1):
                print(f"{idx}. {task} -- {status}\n")
    elif userinput == 2:
        for idx, (task, status) in enumerate(status_dict.items(), 1):
            if status == "Uncompleted":
                print(f"{idx}. {task} -- {status}\n")
    elif userinput == 3:
        for idx, (task, status) in enumerate(status_dict.items(), 1):
            if status == "completed":
                print(f"{idx}. {task} -- {status}\n")

    elif userinput == 4:
        while True:
            counter = 1
            print(colors.SEA_BLUE + "\nCurrent Tasks: " + colors.ENDC)
            for task, status in status_dict.items():
                print(f"{counter} - Task: {task} | Status: {status}\n")
                counter += 1

            edit = input(
                colors.BOLD + "\nEnter the task number to toggle status" + colors.BOLD + " (or 'q' to quit): " + colors.ENDC).strip()

            if edit.lower() == 'q':
                break  # Exit the edit loop

            try:
                edit = int(edit)
                if 1 <= edit <= len(status_dict):
                    task_list = list(status_dict.keys())
                    selected_task = task_list[edit - 1]

                    # Toggle status
                    new_status = "Uncompleted" if status_dict[selected_task] == "completed" else "completed"
                    status_dict[selected_task] = new_status
                    print(colors.SEA_BLUE + f"\nTask '{selected_task}' updated to '{new_status}'!")
                    my_app()
                else:
                    print(colors.ALERT_RED + "Invalid task number. Please try again. " + colors.ENDC)
            except ValueError:
                print(colors.ALERT_RED + "Invalid input. Enter a number or 'q' to quit. " + colors.ENDC)
        print(status_dict)
    elif userinput == 5:
        my_app()


def remove_task():
    counter = 1
    for i in tasks:
        print(f'{counter}- {i}')
        counter += 1
    while True:
        try:
            usr_input = int(input(
                colors.DANGER_RED + "\nEnter the number of task you want to delete or Type 0 to return to the previous menu \n >> " + colors.ENDC))
            if usr_input == 0:
                my_app()
            tasks.pop(usr_input - 1)
            break
        except ValueError:
            print(colors.ALERT_RED + "Invalid input. Please enter a number from the list." + colors.ENDC)
        except IndexError:
            print(colors.ALERT_RED + "Invalid input. Please enter a number from the list." + colors.ENDC)
    for idx, (task, status) in enumerate(status_dict.items(), 1):
        print(f"{idx}. {task} -- {status}\n")


def my_app():
    while True:
        try:
            print(
                colors.SKY_BLUE + " 1-Add tasks \n" + colors.OCEAN_BLUE + " 2-Preview tasks \n" + colors.AQUA + " 3-Remove tasks \n" + colors.EXIT_COLOR + " 4-Exit " + colors.ENDC)
            usr = int(
                input(colors.SKY_BLUE + "Please choose an option by entering the corresponding number: " + colors.ENDC))
            if usr == 1:
                add_task()
                mapping()
            elif usr == 2:
                preview()
                mapping()
            elif usr == 3:
                remove_task()
                mapping()
            elif usr == 4:
                break
            else:
                print(colors.ALERT_RED + "Invalid input. Please enter a number within the range." + colors.ENDC)
                continue
        except ValueError:
            print(colors.ALERT_RED + "Invalid input. Please enter a number." + colors.ENDC)


my_app()