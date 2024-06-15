tasks = []

def display_tasks():
    if not tasks:
        print("Sorry. It's Empty")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{idx}. {task['description']} [{status}]")

def add_task():
    description = input("Enter task description: ")
    tasks.append({"description": description, "completed": False})

def update_task():
    display_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        if 0 < task_num <= len(tasks):
            new_description = input("Enter new description: ")
            tasks[task_num - 1]['description'] = new_description
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_completed():
    display_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTask Process:")
        print("1. Set My Task")
        print("2. Upgrade My Task")
        print("3. Delete My Task")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                update_task()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

