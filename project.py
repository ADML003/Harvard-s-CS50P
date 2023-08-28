def add_task(tasks, task):
    tasks.append(task)
    return tasks

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        return tasks
    else:
        print("Invalid task index.")
        return tasks

def view_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def main():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks = add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
            index = int(input("Enter the task index to complete: ")) - 1
            tasks = complete_task(tasks, index)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
