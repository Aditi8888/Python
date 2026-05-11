contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName  : {name}")
        print(f"Phone : {info['phone']}")
        print(f"Email : {info['email']}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def view_all():
    if not contacts:
        print("No contacts found.")
        return
    print(f"\n{'Name':<20} {'Phone':<15} {'Email'}")
    print("-" * 50)
    for name, info in contacts.items():
        print(f"{name:<20} {info['phone']:<15} {info['email']}")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. View all contacts")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

main()