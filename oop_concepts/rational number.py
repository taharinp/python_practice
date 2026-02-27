class Rational:

    def __init__(self, num, den):
        self.num = num
        self.den = den

    # for printing
    def __str__(self):
        return f"{self.num}/{self.den}"

    # addition
    def __add__(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        return Rational(n, d)

    # multiplication
    def __mul__(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Rational(n, d)


# objects
r1 = Rational(1, 2)
r2 = Rational(3, 4)

print("First:", r1)
print("Second:", r2)

print("Addition:", r1 + r2)
print("Multiplication:", r1 * r2)