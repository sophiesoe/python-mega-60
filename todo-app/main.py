todos = ["clean"]

def print_todos():
  if len(todos) == 0:
     print("No todos added.")
  for index, todo in enumerate(todos, start=0):
        print(f"{index + 1}. {todo.title()}")


while True:
  user_action = input("Type add, show, edit, complete or exit\n").strip()
  match user_action:
    case "add":
      todo = input("Enter todo: ")
      todos.append(todo)
    case "show":
      print_todos()
    case "edit":
      print_todos()
      if len(todos) > 0:     
        todo_item = input("Number of todo to edit: ")
        todo_index = int(todo_item) -1
        if(todo_index < len(todos)):
          editTodo = input(f"Todo: {todos[todo_index].title()}\nType edit todo: ")
          todos[todo_index] = editTodo
          print_todos()
        else: print("No todo found with this number.")
      else: print("Empty todos")
    case "complete":
        print_todos()
        todo_item = input("Number of todo to complete: ")
        todo_index = int(todo_item) -1
        if(todo_index < len(todos)):
          todos.pop(todo_index)
          if len(todos) == 0:
              print("You have finished all todos!")
          else: print_todos()
        else: print("No todo found with this number.")
    case "exit":
      break
    
print("Bye!")