class Payment:
    def process_payment(self):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card Payment of {amount}...Payment Successful")
    
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal Payment  of {amount}...Payment Successful")

class BitcoinPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Bitcoin Payment of {amount}...Payment Successful")

def main():
    credit_card = CreditCardPayment()
    credit_card.process_payment(1000)
    print()
    paypal = PayPalPayment()
    paypal.process_payment(2000)
    print()
    bitcoin = BitcoinPayment()
    bitcoin.process_payment(300)

main()


