
tasks = []
status_dict ={}
def handle_input():
    while True:
        try:
           usrin = int(input("enter a valid number"))
        except ValueError:
            print("please enter a number")
        except IndexError:
            print("please enter a number")
        return usrin


def mapping():
    for task in tasks:
        if task in status_dict.values():
            continue
        status_dict[task] = 'Uncompleted task'
    for i in list(status_dict.keys()):
        if i not in tasks:
            status_dict.pop(i)
    print(status_dict)

def add_task():
    try:
        new_task = input("enter a task / to go back write 0 ")
        if new_task == 0:
            my_app()
    except ValueError:
        print('asfsff')
    tasks.append(new_task)
    print(f"your {new_task} task has been added")

def preview():
    userinput= int(input("1-show all tasks \n 2- uncompleted tasks \n completed tasks \n change status"))
    if userinput == 1:
        print(tasks)
    elif userinput == 2:
        for task,status  in status_dict.items():
            if status == "Uncompleted task":
                print(f"-{task}")
    elif userinput == 3:
        for task,status  in status_dict.items():
            if status == "completed task":
                print(f"-{task}")

    elif userinput == 4:
        while True:
            counter = 1
            print("\nCurrent Tasks:")
            for task, status in status_dict.items():
                print(f"{counter} - Task: {task} | Status: {status}")
                counter += 1

            edit = input("\nEnter the task number to toggle status (or 'q' to quit): ").strip()

            if edit.lower() == 'q':
                break  # Exit the edit loop

            try:
                edit = int(edit)
                if 1 <= edit <= len(status_dict):
                    task_list = list(status_dict.keys())
                    selected_task = task_list[edit - 1]

                    # Toggle status
                    new_status = "uncompleted" if status_dict[selected_task] == "completed" else "completed"
                    status_dict[selected_task] = new_status
                    print(f"\nTask '{selected_task}' updated to '{new_status}'!")
                    my_app()
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Invalid input. Enter a number or 'q' to quit.")
def remove_task():
    counter = 1
    for i in tasks:
        print(f'{counter}-{i}')
        counter += 1
    while True:
        try:
            usr_input = int(input("choose a number write 0 to back"))
            if usr_input == 0:
                my_app()
            tasks.pop(usr_input - 1)
            break
        except ValueError:
            print("please enter a number")
        except IndexError:
            print("please enter a number")
    print(tasks)


def my_app():
    while True:
        print("1-Add tasks \n 2-remove tasks \n 3-preview tasks \n 4-Exit ")
        usr = int(input("enter a number"))
        if usr == 1:
            add_task()
            mapping()
        elif usr == 2:
            remove_task()
            mapping()
        elif usr == 3:
            preview()
            mapping()
        elif usr == 4:
            break
        else:
            continue
my_app()