import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append("\n"+new_todo)
    function.write_todos(todos)

def delete_item():
    todos.pop()

st.title("My to do app")
st.subheader("This is my todo app")
st.write("This app to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='',placeholder = "Add new todo...",on_change =add_todo,key='new_todo')
st.button('Delete')

# st.session_state