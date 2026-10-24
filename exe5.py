class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ").strip().title()
        if not name:
            return print("Name cannot be empty!")
            
        try:
            score = float(input("Enter student score: "))
            if not (0 <= score <= 20):
                return print("Score must be between 0 and 20!")
                
            self.students.append({"name": name, "score": score})
            print(f"Student '{name}' added successfully!")
        except ValueError:
            print("Invalid score! Please enter a number.")

    def show_students(self):
        if not self.students:
            return print("No students found.")
            
        print("\n--- Student List ---")
        for i, student in enumerate(self.students, start=1):
            print(f"{i}. {student['name']} : {student['score']}")

    def calculate_average(self):
        if not self.students:
            return print("No students to calculate average.")
            
        total = sum(student["score"] for student in self.students)
        avg = total / len(self.students)
        print(f"\nClass Average: {avg:.2f}")

    def find_top_student(self):
        if not self.students:
            return print("No students found.")
            
        top = max(self.students, key=lambda x: x["score"])
        print(f"\nTop Student: {top['name']} with score {top['score']}")

    def run(self):
        while True:
            print("\n1. Add | 2. Show | 3. Average | 4. Top Student | 5. Exit")
            choice = input("Choose: ")
            
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.show_students()
            elif choice == "3":
                self.calculate_average()
            elif choice == "4":
                self.find_top_student()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

if __name__ == "__main__":
    StudentManager().run()
