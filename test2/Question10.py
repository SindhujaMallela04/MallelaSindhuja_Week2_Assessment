class Electronics:
    def __init__(self, type, brand):
        self.type = type
        self.brand = brand

    def display(self):
        print(f"Type : {self.type}")
        print(f"Brand: {self.brand}")

class MobileDevice(Electronics):
    def __init__(self, type, brand, connection_type):
        super().__init__(type, brand)
        self.connection_type = connection_type

    def connect(self):
        print(f"{self.brand} device is connecting via {self.connection_type}")

    def display(self):
        super().display()
        print(f"Connection Type : {self.connection_type}")

class SmartPhone(MobileDevice):
    def __init__(self, type, brand, connection_type, camera_resolution):
        super().__init__(type, brand, connection_type)
        self.camera_resolution = camera_resolution

    def connect(self):
        print(f"{self.brand} device is connecting via {self.connection_type}")

    def display(self):
        super().display()
        print(f"The camera resolution is {self.camera_resolution} Mega Pixels")

def main():
    mobile_device = MobileDevice("hand-held", "Nokia", "WI-FI")
    mobile_device.connect()
    mobile_device.display()
    print()

    smart_phone = SmartPhone("hand-held", "Samsung", "5G", 64)
    smart_phone.connect()
    smart_phone.display()
main()



    