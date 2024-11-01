# Contact Book Application
import json

# File to save contacts data
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

# View all contacts
def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
    else:
        print("No contacts available.")

# Search contacts by name or phone number
def search_contact(contacts):
    query = input("Enter Name or Phone Number to search: ")
    results = [contact for contact in contacts if query in contact["name"] or query in contact["phone"]]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print("No contact found.")

# Update an existing contact
def update_contact(contacts):
    name = input("Enter the Name of the contact to update: ")
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = input(f"Enter new Phone Number ({contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"Enter new Email ({contact['email']}): ") or contact["email"]
            contact["address"] = input(f"Enter new Address ({contact['address']}): ") or contact["address"]
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the Name of the contact to delete: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

# Main Menu
def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
