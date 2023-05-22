import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", 'w') as file:
        pass
sg.theme("DarkTeal2")

# GUI Objects
clock_label = sg.Text('', key='clock')
label = sg.Text("Type in todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todoInputBox", size=[20])
# add_button = sg.Button(image_source="add.png", mouseover_colors='Green', key='Add')
add_button = sg.Button("Add", key='Add')
list_box = sg.Listbox(values=functions.get_todolist(), key="todosList", enable_events=True, size=[20, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
prompt_label = sg.Text(key="prompt")

window = sg.Window('My todo window',
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, prompt_label]],
                   font=('Helvetica', 16))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%A %d %B, %Y %H:%M:%S"))
    # print(1, event)
    # print(2, values)
    match event:
        case "Add":
            todoList = functions.get_todolist()
            new_todo = values['todoInputBox'] + "\n"
            todoList.append(new_todo)
            functions.write_todolist(todoList)

            window['todosList'].update(values=functions.get_todolist())

        case "Edit":
            try:
                todo_to_edit = values['todosList'][0]
                new_todo = values['todoInputBox']

                todoList = functions.get_todolist()
                index = todoList.index(todo_to_edit)
                todoList[index] = new_todo + "\n"

                functions.write_todolist(todoList)
                window['todosList'].update(values=functions.get_todolist())
            except IndexError:
                prompt_label.update(value="Please Select a Value")
        case "Complete":
            try:
                todo_to_complete = values['todosList'][0]
                todoList = functions.get_todolist()
                todoList.remove(todo_to_complete)

                functions.write_todolist(todoList)
                window['todosList'].update(values=functions.get_todolist())
                window['todoInputBox'].update(value='')
            except IndexError:
                sg.popup_error("Please Select a Value", font=('Helvetica', 16))

            # functions.refresh_window(window='todosList')

        case "Exit":
            break
        case 'todosList':
            window['todoInputBox'].update(value=values['todosList'][0])
        case sg.WINDOW_CLOSED:
            break
window.close()
