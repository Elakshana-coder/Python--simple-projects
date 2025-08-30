tasks = []
while True:
    print("\n---📝TO-DO LIST ---")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Delete Tasks")
    print("4. Exit")

    choice = input("Enter choice(1-4):")

    if choice == "1":
        task = input("Enter a new task :")
        tasks.append(task)
        print("Task added successfully")

    elif choice =="2":
        if tasks:
            print("\n📋Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task}")

        else:
            print("No tasks found!")

    elif choice == "3":
        if tasks:
            task_no = int(input("Enter task number to delete:"))
            if 0 < task_no <= len(tasks):
                removed = tasks.pop(task_no -1)
                print(f"task'{removed}'deleted!")

            else:
                print("Invalid Number")
        else:
            print("No task to delete")

    elif choice =="4":
        print("GoodBye Stay productive !")
        break
    else:
        print("Invalid choice try again")
        
                          
