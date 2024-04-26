

todos =[]

while True:
    user_action = input("Type add, show/display, edit or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a To-do Activity: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("Number of the to-do item"))
            number = number-1
            new_todo = input("Enter a new to-do:")
            todos[number] = new_todo
        case 'exit':
            break
        case x:
            print("Kya kar raha hai bhai tu?")

print('bye')


