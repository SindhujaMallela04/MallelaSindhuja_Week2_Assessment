class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}")

class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model

    def display(self):
        super().display()
        print(f"Model: {self.model}")

class Bike(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model

    def display(self):
        super().display()
        print(f"Model: {self.model}")

class ElectricCar(Car):
    def __init__(self, name, color, model, battery):
        super().__init__(name, color, model)
        self.battery = battery

    def display(self):
        super().display()
        print(f"Battery: {self.battery}")

def main():
    car = Car("Lamorghini", "Red", "Gallado")
    car.display()
    print()
    bike = Bike("Mini", "Blue", "Cooper")
    bike.display()
    print()
    electric_car = ElectricCar("Kia", "Silver", "EV6", "100 kWh")
    electric_car.display()
main()
