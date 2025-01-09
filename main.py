# Simple To-Do List Manager
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Done")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, (task, done) in enumerate(tasks, start=1):
            status = "Done" if done else "Pending"
            print(f"{i}. {task} - {status}")

def add_task(tasks):
    task = input("\nEnter the task: ")
    tasks.append((task, False))
    print(f"Task '{task}' added!")

def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("\nEnter the task number to mark as done: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1] = (tasks[task_no - 1][0], True)
                print(f"Task {task_no} marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            print("\nExiting To-Do List Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
