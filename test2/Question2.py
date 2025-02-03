class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount of {amount} has been deposited.")
        print(f"Balance in the account is {self.__balance}")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
            print("Balance in Account: ", self.__balance)
        else:
            self.__balance -= amount
            print(f"Amount of {amount} has been withdrawn.")
            print(f"Balance in the account is {self.__balance}")

def main():
    print("welcome to the ABC Bank")
    print()
    print("Deposit some money to start using your account")
    account = BankAccount()
    while(1):
        print()
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Exit")
        print("Enter your choice: ")
        choice = int(input())        
        if(choice == 1):
            amount = int(input("Enter the amount to deposit : "))
            if amount < 0:
                print("Invalid amoount. AMount should be greater than 0")
            else:
                account.deposit(amount)
        elif(choice == 2):
            amount = int(input("Enter the amount to withdraw : "))
            account.withdraw(amount)
        elif choice == 3:
            break
        else:
            print("Invalid Choice, Try Again")
main()
