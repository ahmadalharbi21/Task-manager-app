import streamlit as st
class colors:
    # Blue
    m = '\033[38;5;32m'
    SEA_BLUE = m
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


if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'status_dict' not in st.session_state:
    st.session_state.status_dict = {}


def mapping():
    for task in st.session_state.tasks:
        if task in st.session_state.status_dict.values():
            continue
        st.session_state.status_dict[task] = 'Uncompleted'
    for i in list(st.session_state.status_dict.keys()):
        if i not in st.session_state.tasks:
            st.session_state.status_dict.pop(i)


def add_tasks():
    with st.form("Add Tasks"):
        st.subheader("Add New Task")
        new_task = st.text_input("Enter your task (type 0 to cancel)")
        submitted = st.form_submit_button("Add Task")

        if submitted:
            if new_task and new_task != '0':
                st.session_state.tasks.append(new_task)
                mapping()
                st.success(f"Task '{new_task}' added successfully!")
                st.write(st.session_state.tasks)
            elif new_task == '0':
                st.info("Operation cancelled")

def preview():
    tab1, tab2 ,tab3= st.tabs(["All","completed", "incompleted"])  # Tabs
    st.write("hello")
    with tab1:
        if len(st.session_state.tasks) == 0:
            st.write("no tasks yet")
        else:
            print(colors.SEA_BLUE + "\n-- Current Tasks --\n" + colors.ENDC)
            for idx, (task, status) in enumerate(st.session_state.status_dict.items(), 1):
                st.write(f"{idx}. {task} -- {status}\n")
    with tab2:
        st.write(st.session_state.tasks)
    with tab3:
        for idx, (task, status) in enumerate(st.session_state.status_dict.items(), 1):
            if status == "completed":
                st.write(f"{idx}. {task} -- {status}\n")

    # elif:
    #     while True:
    #         counter = 1
    #         print(colors.SEA_BLUE + "\nCurrent Tasks: " + colors.ENDC)
    #         for task, status in status_dict.items():
    #             print(f"{counter} - Task: {task} | Status: {status}\n")
    #             counter += 1
    #
    #         edit = input(
    #             colors.BOLD + "\nEnter the task number to toggle status" + colors.BOLD + " (or 'q' to quit): " + colors.ENDC).strip()
    #
    #         if edit.lower() == 'q':
    #             break  # Exit the edit loop
    #
    #         try:
    #             edit = int(edit)
    #             if 1 <= edit <= len(status_dict):
    #                 task_list = list(status_dict.keys())
    #                 selected_task = task_list[edit - 1]
    #
    #                 # Toggle status
    #                 new_status = "Uncompleted" if status_dict[selected_task] == "completed" else "completed"
    #                 status_dict[selected_task] = new_status
    #                 print(colors.SEA_BLUE + f"\nTask '{selected_task}' updated to '{new_status}'!")
    #             else:
    #                 print(colors.ALERT_RED + "Invalid task number. Please try again. " + colors.ENDC)
    #         except ValueError:
    #             print(colors.ALERT_RED + "Invalid input. Enter a number or 'q' to quit. " + colors.ENDC)
    #     print(status_dict)

def remove_task():
    counter = 1
    for i in st.session_state.tasks:
        print(f'{counter}- {i}')
        counter += 1
    while True:
        try:
            usr_input = int(input(
                colors.DANGER_RED + "\nEnter the number of task you want to delete or Type 0 to return to the previous menu \n >> " + colors.ENDC))
            st.session_state.tasks.pop(usr_input - 1)
            break
        except ValueError:
            print(colors.ALERT_RED + "Invalid input. Please enter a number from the list." + colors.ENDC)
        except IndexError:
            print(colors.ALERT_RED + "Invalid input. Please enter a number from the list." + colors.ENDC)
    for idx, (task, status) in enumerate(st.session_state.status_dict.items(), 1):
        print(f"{idx}. {task} -- {status}\n")


def main():
    st.set_page_config(page_title="Task Manager", layout="wide")
    st.title("Task manager app")
    page = st.sidebar.radio("Navigation", ["Add Task", "Remove Task", "View Tasks"])
    try:
       # print(
        #colors.SKY_BLUE + " 1-Add tasks \n" + colors.OCEAN_BLUE + " 2-Preview tasks \n" + colors.AQUA + " 3-Remove tasks \n" + colors.EXIT_COLOR + " 4-Exit " + colors.ENDC)
        #usr = st.text_input(colors.SKY_BLUE + "Please choose an option by entering the corresponding number: " + colors.ENDC)
        if page == "Add Task":
            add_tasks()
            mapping()
        elif page == "Remove Task":
            remove_task()
            mapping()
        elif page == "View Tasks":
            preview()
            mapping()
    except ValueError:
        print(colors.ALERT_RED + "Invalid input. Please enter a number." + colors.ENDC)


if __name__ == "__main__":
    main()