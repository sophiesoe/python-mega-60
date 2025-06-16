
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
  match user_action:
    case "add":
      todo = input("Enter todo: ") + "\n"
      addTodo(todo)
    case "show":
      todos = readFile()
      print_todos(todos)
    case "edit":
      todos = readFile()
      print_todos(todos)

      if len(todos) > 0:     
        todo_item = input("Number of todo to edit: ")
        todo_index = int(todo_item) -1
        if(todo_index < len(todos)):
          editTodo = input(f"Todo: {todos[todo_index].title()}\nType edit todo: ") + "\n"
          todos[todo_index] = editTodo
          writeTodo(todos)
          todos = readFile()
          print_todos(todos)
        else: print("No todo found with this number.")
      else: print("Empty todos")
    case "complete":
        todos = readFile()
        print_todos(todos)
        todo_item = input("Number of todo to complete: ")
        todo_index = int(todo_item) -1
        if(todo_index < len(todos)):
          todos.pop(todo_index)
          if len(todos) == 0:
              print("You have finished all todos!")
          else: 
            todos = readFile()
            print_todos(todos)
        else: print("No todo found with this number.")
    case "exit":
      break
    
print("Bye!")