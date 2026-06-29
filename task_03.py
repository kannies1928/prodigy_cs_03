import json
import os

FILE_NAME = "contacts.json"

# Load contacts
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contacts.append({
        "Name": name,
        "Phone": phone,
        "Email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!\n")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n----- Contact List -----")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name : {contact['Name']}")
        print(f"   Phone: {contact['Phone']}")
        print(f"   Email: {contact['Email']}")
        print()

# Edit contact
def edit_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    index = int(input("Enter contact number to edit: ")) - 1

    if 0 <= index < len(contacts):
        contacts[index]["Name"] = input("Enter New Name: ")
        contacts[index]["Phone"] = input("Enter New Phone: ")
        contacts[index]["Email"] = input("Enter New Email: ")

        save_contacts(contacts)
        print("Contact updated successfully!\n")
    else:
        print("Invalid contact number.\n")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    index = int(input("Enter contact number to delete: ")) - 1

    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!\n")
    else:
        print("Invalid contact number.\n")

# Main program
def main():
    contacts = load_contacts()

    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Thank you for using Contact Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()