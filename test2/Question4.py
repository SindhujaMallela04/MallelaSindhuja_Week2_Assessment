class Student:
    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no
    def get_name(self):
        return self.__name
    def get_roll_no(self):
        return self.__roll_no

def get_input():
    student_name = input("Enter the student name: ")
    student_roll_no = int(input("Enter the student roll number: "))
    return student_name, student_roll_no  
  
def main():
    student_name, student_roll_no = get_input()
    student = Student(student_name, student_roll_no)
    print(f"Student Name: {student.get_name()}")
    print(f"Student Roll Number: {student.get_roll_no()}")
main()
    