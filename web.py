import streamlit as st
import functions

todolist = functions.get_todolist()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todolist.append(todo)
    functions.write_todolist(todolist)


st.title("My Todo App")
st.subheader("this application adds todo items")
st.write("This app is to help increase your <b>productivity</b>", unsafe_allow_html=True)


for index, todo in enumerate(todolist):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todolist.pop(index)
        functions.write_todolist(todolist)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new item", on_change=add_todo, key='new_todo')

st.session_state