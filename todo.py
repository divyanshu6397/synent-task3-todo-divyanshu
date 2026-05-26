tasks = []

print("===== TO-DO LIST APPLICATION =====")

while True:
    print("\nChoose an Option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    option = input("Enter your choice (1-4): ")

    if option == "1":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added successfully!")

    elif option == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif option == "3":
        if len(tasks) == 0:
            print("Task list is empty.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            try:
                delete_num = int(input("Enter task number to delete: "))

                if 1 <= delete_num <= len(tasks):
                    removed_task = tasks.pop(delete_num - 1)
                    print(f"Task '{removed_task}' deleted.")
                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number.")

    elif option == "4":
        print("Application Closed.")
        break

    else:
        print("Invalid choice! Try again.")