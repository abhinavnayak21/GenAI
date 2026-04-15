# Task 5: Abstraction

class Payment:
    def process_payment(self, amount):
        pass  # abstract-like method


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Paid", amount, "using Credit Card")


class UPIPayment(Payment):
    def process_payment(self, amount):
        print("Paid", amount, "using UPI")


# Test
p1 = CreditCardPayment()
p2 = UPIPayment()

p1.process_payment(1000)
p2.process_payment(500)