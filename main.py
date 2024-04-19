

todos =[]

while True:
    user_action = input("Type add, show or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a To-do Activity: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print('bye')


