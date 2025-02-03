class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, age, emp_id, dept):
        super().__init__(name, age, emp_id)
        self.dept = dept

    def display(self):
        super().display()
        print(f"Manager of {self.dept} department")

    def approve_leave(self, days):
        print(f"Manager {self.name} has approved leave for {days} days.")

def main():
    emp = Employee("Suresh", 30, "E01")
    emp.display()
    print()
    manager = Manager("Ramesh", 35, "M01", "HR")
    manager.display()
    manager.approve_leave(2)
main()