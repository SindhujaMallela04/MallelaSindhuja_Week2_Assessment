class Animal:
    def type (self):
        pass
    def speak(self):
        pass

class Dog(Animal):
    def type(self):
        print("This is a Dog.")
    def speak(self):
        print("A Dog Barks.")

class Cat(Animal):
    def type(self):
        print("This is a Cat")
    def speak(self):
        print("A Cat says Meow")

def main():
    dog = Dog()
    dog.type()
    dog.speak()
    print()
    cat = Cat()
    cat.type()
    cat.speak()
main()