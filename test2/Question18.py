from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def subtract(self):
        pass
    
    @abstractmethod
    def multiply(self):
        pass
    
    @abstractmethod
    def divide(self):
        pass

class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
def main():
    basic_calculator = BasicCalculator()
    print(f"Addition : 3 + 4 = {basic_calculator.add(3, 4)}")
    print(f"Subtraction : 3 - 4 = {basic_calculator.subtract(3, 4)}")
    print(f"Multiplication : 3 x 4 = {basic_calculator.multiply(3, 4)}")
    print(f"Division : 3 / 4 = {basic_calculator.divide(3, 4)}")
main()