# To-Do List CLI (updated version)
tasks = []

# Function to show all tasks
def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task
def add_task():
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty!")

# Function to delete a task
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    show_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task '{removed}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    print("\nTo-Do List Options:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting To-Do List. Bye!")
        break
    else:
        print("Invalid choice. Try again.")