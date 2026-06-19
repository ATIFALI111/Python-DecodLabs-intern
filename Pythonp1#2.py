tasks = []

def add_task():

    title = input("Task Title: ")
    category = input("Category: ")
    priority = input("Priority (High/Medium/Low): ")

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "category": category,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)

    print("\nTask Added Successfully!")

def view_tasks():

    if not tasks:
        print("\nNo Tasks Available")
        return

    print("\n~~~~~~~ TASK LIST ~~~~~~~")

    for task in tasks:

        print(f"""
ID       : {task['id']}
Title    : {task['title']}
Category : {task['category']}
Priority : {task['priority']}
Status   : {task['status']}
--------------------------------
""")

while True:

    print("""
~~~~~~ TO DO LIST ~~~~~~

1. Add Task
2. View Tasks
3. Exit
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")




add_task()
