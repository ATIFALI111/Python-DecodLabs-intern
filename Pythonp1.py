def to_do_list():
    tasks = []


    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Quit")
        choice = input("Choice: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully.")

        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"Task '{task}' removed successfully.")
            else:
                print("Task does not exist.")

        elif choice == "3":
            if tasks:
                print("\nYour Tasks:")
                for t in tasks:
                    print(f"- {t}")
            else:
                print("Your to-do list is empty.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")


to_do_list()

