import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("\n📌 No tasks available!\n")
        return
    print("\n📋 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {status} {task['task']}")

def add_task(tasks):
    task_name = input("Enter task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("✅ Task added successfully!")

def mark_task_done(tasks):
    display_tasks(tasks)
    try:
        task_no = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_no < len(tasks):
            tasks[task_no]["done"] = True
            save_tasks(tasks)
            print("✔ Task marked as done!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Please enter a valid number!")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_no = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_no < len(tasks):
            removed_task = tasks.pop(task_no)
            save_tasks(tasks)
            print(f"🗑 Task '{removed_task['task']}' deleted successfully!")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Please enter a valid number!")

def main():
    tasks = load_tasks()
    while True:
        print("\n📌 To-Do List App")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Mark Task as Done")
        print("4️⃣ Delete Task")
        print("5️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
