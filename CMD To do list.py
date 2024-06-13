def display_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Update Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task(tasks):
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_index] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
