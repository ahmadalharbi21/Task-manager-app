import streamlit as st
if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'status_dict' not in st.session_state:
    st.session_state.status_dict = {}


def mapping():
    for task in st.session_state.tasks:
        if task in st.session_state.status_dict.values():
            continue
        st.session_state.status_dict[task] = 'Incompleted'
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
            elif new_task == '0':
                st.info("Operation cancelled")

def preview():
    tab1, tab2 ,tab3= st.tabs(["All","Completed", "Incompleted"])  # Tabs
    with tab1:
        if len(st.session_state.tasks) == 0:
            st.write("no tasks yet")
        else:
            st.write("\n-- Current Tasks --\n")
            for idx, (task, status) in enumerate(st.session_state.status_dict.items(), 1):
                agree = st.checkbox(f"{idx}. {task}\n")
                if agree:
                    new_status = "Incomplete" if st.session_state.status_dict[task] == "Completed" else "Completed"
                    st.session_state.status_dict[task] = new_status
    with tab2:
        for idx, (task, status) in enumerate(st.session_state.status_dict.items(), 1):
            if status =="Completed":
                st.write(f"{idx}. {task} -- {status}\n")
    with tab3:
        for idx, (task, status) in enumerate(st.session_state.status_dict.items(), 1):
            if status == "Incompleted":
                st.write(f"{idx}. {task} -- {status}\n")

def remove_task():
    # Create columns to display each task in a row
    for counter, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])  # 4 for task text and 1 for the button

        with col1:
            st.write(f'{counter}- {task}')

        with col2:
            if st.button(f'Remove {counter}', key=f'button{counter}'):
                st.session_state.tasks.remove(task)

def main():
    st.set_page_config(page_title="Task Manager", layout="wide")
    st.title("Task manager app")
    page = st.sidebar.radio("Navigation", ["Add Task", "Remove Task", "View Tasks"])
    try:
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
        st.write("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()