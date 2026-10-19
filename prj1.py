import json

# ==========================================
# ۱. قالب مخاطب (کلاس)
# ==========================================
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# ==========================================
# ۲. مغز متفکر برنامه (مدیریت)
# ==========================================
class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                self.contacts = [Contact(item["name"], item["phone"]) for item in data]
        except FileNotFoundError:
            pass

    def save_contacts(self):
        data = [{"name": c.name, "phone": c.phone} for c in self.contacts]
        with open("contacts.json", "w") as file:
            json.dump(data, file)

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        self.contacts.append(Contact(name, phone))
        self.save_contacts()
        print("Contact added!")

    def show_contacts(self):
        print("\n--- Contacts ---")
        for i, c in enumerate(self.contacts, start=1):
            print(f"{i}. {c.name} : {c.phone}")
        print("----------------")

    def run(self):
        while True:
            print("\n1. Add | 2. Show | 3. Exit")
            choice = input("Choose: ")
            
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.show_contacts()
            elif choice == "3":
                break


# ==========================================
# ۳. اجرای برنامه
# ==========================================
app = ContactManager()
app.run()
