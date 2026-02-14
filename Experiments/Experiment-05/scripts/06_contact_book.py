# Contact book using dictionary
contacts = {}

while True:
    print("1. Add  2. Search  3. Update  4. Delete  5. View  6. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        contacts[name] = phone
    elif choice == "2":
        name = input("Name to search: ").strip()
        print("Phone:", contacts.get(name, "Not found"))
    elif choice == "3":
        name = input("Name to update: ").strip()
        if name in contacts:
            contacts[name] = input("New phone: ").strip()
        else:
            print("Not found")
    elif choice == "4":
        name = input("Name to delete: ").strip()
        contacts.pop(name, None)
    elif choice == "5":
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == "6":
        break
    else:
        print("Invalid choice")
