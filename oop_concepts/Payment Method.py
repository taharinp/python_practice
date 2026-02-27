class CreditCard:

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI:

    def pay(self, amount):
        print("Paid", amount, "using UPI")


class Cash:

    def pay(self, amount):
        print("Paid", amount, "using Cash")


# objects
p1 = CreditCard()
p2 = UPI()
p3 = Cash()


p1.pay(1000)
p2.pay(500)
p3.pay(200)