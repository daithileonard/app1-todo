FILEPATH = "todo.txt"


def get_todolist(filepath=FILEPATH):
    """Read the text file and return the list items"""
    with open(filepath, 'r') as file_local:
        todolist_local = file_local.readlines()
    return todolist_local


def write_todolist(todolist_local, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todolist_local)


def refresh_window(window_local):
    window_local['todosList'].update(values=get_todolist())


if __name__ == "__main__":
    print("Functions have been accessed")
