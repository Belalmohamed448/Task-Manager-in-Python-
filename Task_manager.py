from datetime import datetime
tasks = []
def add_task():
    title = input("Enter the title of the task: ")
    deadline = input("Enter the deadline of the task (YYYY-MM-DD): ")
    created_date = datetime.now()

    while True:
        priority = input("Enter priority (High/Medium/Low): ").capitalize()

        if priority in ["High", "Medium", "Low"]:
            break

        print("Invalid priority. Please enter High, Medium, or Low.")

    task = {
        "title": title,
        "deadline": deadline,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)

    print(f"Task '{task['title']}' added successfully")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_tasks = sorted(
        tasks,
        key=lambda task: priority_order[task["priority"]]
    )

    print("Tasks:")

    for i, task in enumerate(sorted_tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(
            f"{i}. {task['title']} - "
            f"Priority: {task['priority']} - "
            f"Deadline: {task['deadline']} - "
            f"Status: {status} - "
            f"Created: {task['created_at']}"
        )
def mark_task_completed():
    if len(tasks) == 0:
        print ("No Tasks available to be marked as completed")
       
        return
    view_tasks()
    task_num=input("Enter the task number to mark as completed: ")
    if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
        index = int(task_num) - 1
        if tasks[index]["completed"]:
            print(f"Task '{tasks[index]['title']}' is already marked as completed.")
        else:
            tasks[index]["completed"] = True
            print(f"Task '{tasks[index]['title']}' marked as completed.")
    else:
            print("Invalid task number.")


def delete_task():
    if len(tasks)==0:
        print ("No Tasks available to delete")
        return 
    
    
    else:
        view_tasks()
        task_num=input("Enter the task number to delete : ")
        if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
            index = int(task_num)-1
            removed_task = tasks.pop(index)

            print(f"Task '{removed_task['title']}' deleted successfully.")
        else:
            print("Invalid task number.")

def menu():
    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            mark_task_completed()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Thank you for using Task Manager!")
            break

        else:
            print("Invalid choice. Please try again.")
menu()


