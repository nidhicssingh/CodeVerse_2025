tasks = []

def show_menu():
    print("\n TO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print(" Task added!")
    elif choice == "2":
        if not tasks:
            print("📭 No tasks found.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            to_remove = int(input("Enter task number to remove: "))
            if 1 <= to_remove <= len(tasks):
                removed = tasks.pop(to_remove - 1)
                print(f" Removed: {removed}")
            else:
                print("Invalid task number.")
    elif choice == "4":
        print(" Goodbye!")
        break
    else:
        print(" Invalid choice. Please try again.")
