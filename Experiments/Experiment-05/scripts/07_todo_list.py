# Todo list manager using list

tasks = []

while True:
    print("1. Add  2. View  3. Remove  4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        task = input("Enter task: ").strip()
        tasks.append(task)
    elif choice == "2":
        if not tasks:
            print("No tasks")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif choice == "3":
        idx = int(input("Enter task number to remove: "))
        if 1 <= idx <= len(tasks):
            tasks.pop(idx - 1)
        else:
            print("Invalid task number")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
