
def print_todos(todos):
  if len(todos) == 0:
     print("No todos added.")
  for index, todo in enumerate(todos, start=0):
        print(f"{index + 1}. {todo.title().strip("\n")}")

def readFile():
  with open("todos.txt", "r") as file:
    todos = file.readlines()
    return todos

def writeTodo(todos):
  with open("todos.txt", "w") as file:
    todos = file.writelines(todos)


def addTodo(todo):
  todos = readFile()
  todos.append(todo)
  writeTodo(todos)
   


while True:
  user_action = input("Type add, show, edit, complete or exit\n").strip()
  if user_action.startswith("add"):
    todo = user_action[4:]
    addTodo(todo)
  if user_action.startswith("show"):
    todos = readFile()
    print_todos(todos)
  if user_action.startswith("edit"):
      todos = readFile()
      print_todos(todos)

      if len(todos) > 0:
        try:     
          todo_item = user_action[4:]
          todo_index = int(todo_item) -1
          if(todo_index < len(todos)):
            editTodo = input(f"Todo: {todos[todo_index].title()}\nType edit todo: ") + "\n"
            todos[todo_index] = editTodo
            writeTodo(todos)
            todos = readFile()
            print_todos(todos)
        except ValueError:
          print("Please type number after edit.")
        else: print("No todo found with this number.")
      else: print("Empty todos")
  if user_action.startswith("complete"):
      todos = readFile()
      print_todos(todos)
      todo_item = user_action[8:]
      todo_index = int(todo_item) -1
      if(todo_index < len(todos)):
        todos.pop(todo_index)
        if len(todos) == 0:
            print("You have finished all todos!")
        else: 
          todos = readFile()
          print_todos(todos)
      else: print("No todo found with this number.")
  if user_action.startswith("exit"):
    break
    
print("Bye!")