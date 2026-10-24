import json

class PasswordManager:
    def __init__(self):
        self.filename = "passwords.json"
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_password(self):
        site = input("Enter site name: ").strip().lower()
        password = input("Enter password: ").strip()
        
        if not site or not password:
            return print("Site and password cannot be empty!")
            
        self.data[site] = password
        self.save_data()
        print(f"Password for '{site}' saved!")

    def get_password(self):
        site = input("Enter site name to search: ").strip().lower()
        if site in self.data:
            print(f"Password for '{site}': {self.data[site]}")
        else:
            print(f"No password found for '{site}'.")

    def delete_password(self):
        site = input("Enter site name to delete: ").strip().lower()
        if site in self.data:
            del self.data[site]
            self.save_data()
            print(f"Password for '{site}' deleted!")
        else:
            print(f"No password found for '{site}'.")

    def run(self):
        while True:
            print("\n1. Add | 2. Get | 3. Delete | 4. Exit")
            choice = input("Choose: ")
            
            if choice == "1": self.add_password()
            elif choice == "2": self.get_password()
            elif choice == "3": self.delete_password()
            elif choice == "4": break

if __name__ == "__main__":
    PasswordManager().run()
