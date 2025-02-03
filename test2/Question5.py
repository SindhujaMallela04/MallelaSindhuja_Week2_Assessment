class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_product_details(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
    
    def check_availability(self, quantity):
        if quantity > self.stock:
            print(f"Insufficient stock. Available stock : {self.stock}")
        else:
            self.stock -= quantity
            print(f"{quantity} items of {self.name} has been purchased.")

def get_input():
    product_name = input("Enter the product you want to purchase: ")
    return product_name

def main():
    products = []
    while(1):
        print()
        print("1. Add a product")
        print("2. Purchase a product")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            product_name = input("Enter the product name: ")
            product_price = int(input("Enter the product price: "))
            product_stock = int(input("Enter the product stock: "))
            product = Product(product_name, product_price, product_stock)
            products.append(product)
            print()
            print(f"Product {product_name} has been added to the catalog.")
        elif choice == 2:
            product_name = get_input()
            flag = 0
            for product in products:
                if product.name == product_name:
                    flag = 1
                    break
            if flag == 0:
                print(f"The product {product_name} is not available in the catalog.")
            else:
                quantity = int(input("Enter the quantity you want to purchase: "))
                product.check_availability(quantity)
        elif choice == 3:
            break
        else:
            print("Invalid Choice. Please try again.")
main()
        

    