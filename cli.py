# from functions import get_todolist, write_todolist
import functions
import time

now = time.strftime(("%A %d %B, %Y %H:%M:%S"))
print(now)
prompt = "Type Add, Show, Edit, Complete or Quit:"

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todolist = functions.get_todolist(filepath='todo.txt')  # e.g. with filepath included with the arguement

        todolist.append(todo+'\n')

        # with open('todo.txt', 'w') as file:
        # file.writelines(todolist)

        functions.write_todolist(todolist)

    elif user_action.startswith("show") or user_action.startswith("display"):

        todolist = functions.get_todolist()

        # list comprehension function, uncomment and replace with todoList in loop below
        # newTodoList = [item.strip('\n') for item in todolist]

        for index, item in enumerate(todolist):
            item = item.title().strip('\n')
            listItem = f"{index + 1}.{item}"
            print(listItem)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todolist = functions.get_todolist()

            newValue = input("Enter new value: ")
            todolist[number] = newValue + '\n'

            functions.write_todolist(todolist)

        except ValueError:
            print("Your input is not recognised")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todolist = functions.get_todolist()

            todo_to_remove = todolist[number - 1].strip('\n')
            todolist.pop(number - 1)

            functions.write_todolist(todolist)

            message = f"Item {todo_to_remove} has been completed"
            print(message)
        except IndexError:
            print("Not a list item number")
            continue
        except ValueError:
            print("Your input is not recognised")
            continue

    elif user_action.startswith("quit"):
        break
    else:
        print("Please enter a valid user action")

print("Program terminated")
