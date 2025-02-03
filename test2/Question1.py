class Employee:
    def __init__(self, name, id, department):
        self.__name = name
        self.__id = id
        self.__department = department

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_department(self):
        return self.__department
    
def get_input():
    name = input("Enter the employee name: ")
    id = input("Enter the employee id: ")
    department = input("Enter the employee department: ")
    return name, id, department

def main():
    name, id, department = get_input()
    employee = Employee(name, id, department)
    print(f"Employee Name: {employee.get_name()}")
    print(f"Employee ID: {employee.get_id()}")
    print(f"Emplyee Department: {employee.get_department()}")
main()


