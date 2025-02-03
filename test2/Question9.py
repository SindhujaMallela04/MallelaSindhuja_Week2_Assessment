class Car:
    def model(self):
        print("This is a Porshe Car.")

    def move(self):
        print("A Car moves on it's 4 wheels.")

class Airplane:
    def model(self):
        print("This is a Boeing 747 Airplane.")
    
    def move(self):
        print("This airplane moves using it's Wings and Engine support.")

class FlyingCar(Car, Airplane):
    def model(self):
        print("This is a Boeing Porshe Flying Car. Only one of it's Kind")

    def move(self, mode = "drive"):
        if mode == "fly":
            print("The Flying Car is in Flight Mode.")
        else:
            print("The Flying Car is in Driving Mode.")

def main():
    flying_car = FlyingCar()
    flying_car.model()
    flying_car.move()
    flying_car.move("fly")
main()
