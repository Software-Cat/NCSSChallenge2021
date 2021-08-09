SUPER_NUMS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
SUB_NUMS = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']


def gcd(a, b):
  """
  Returns the Greatest Common Divisor between `a` and `b`.
  """
  while b:
    a, b = b, a % b
  return a


def lcm(a, b):
    """
    Returns the Lowest Common Multiple between `a` and `b`
    """
    return a * b / gcd(a, b)


class Rational:
    """
    Represents any rational number in fraction form.
    """

    def __init__(self, numerator, denominator=1):
        """
        Initialises a rational number with the given numerator and denominator.
        """
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __eq__(self, other):
        """
        Returns True if the two given Rational numbers are equal.
        """
        properNumerator1 = self.numerator
        properDenominator1 = self.denominator
        properNumerator2 = other.numerator
        properDenominator2 = other.denominator

        gcd1 = gcd(properNumerator1, properDenominator1)
        properNumerator1 = int(properNumerator1 / gcd1)
        properDenominator1 = int(properDenominator1 / gcd1)

        gcd2 = gcd(properNumerator2, properDenominator2)
        properNumerator2 = int(properNumerator2 / gcd2)
        properDenominator2 = int(properDenominator2 / gcd2)

        if properDenominator1 == properDenominator2 and properNumerator1 == properNumerator2:
            return True
        return False

    def __str__(self):
        """
        Returns a string representing this Rational number.
        """
        # Integer part of mixed numeral
        integerPart = int(self.numerator / self.denominator)
        properNumerator = self.numerator - integerPart * self.denominator

        # Simplify
        commonDivisor = gcd(properNumerator, self.denominator)
        properNumerator = int(properNumerator / commonDivisor)
        properDenominator = int(self.denominator / commonDivisor)

        # Mixed numeral creation
        elements = []
        if not integerPart == 0:
            elements.append(str(integerPart))
        elif properNumerator < 0 or properDenominator < 0:
            elements.append("-")
        properNumerator = abs(properNumerator)
        properDenominator = abs(properDenominator)

        if not properNumerator == 0:
            for char in str(properNumerator):
                elements.append(SUPER_NUMS[int(char)])
            elements.append("/")
            for char in str(properDenominator):
                elements.append(SUB_NUMS[int(char)])

        if len(elements) == 0:
            return "0"
        return "".join(elements)

    def __add__(self, other):
        """
        Returns the addition (+) of two Rational numbers.
        """
        numerator1 = self.numerator
        denominator1 = self.denominator
        numerator2 = other.numerator
        denominator2 = other.denominator

        commonMultiple = lcm(denominator1, denominator2)
        multiplier1 = int(commonMultiple / denominator1)
        multiplier2 = int(commonMultiple / denominator2)

        return Rational(numerator1 * multiplier1 + numerator2 * multiplier2, commonMultiple)

    def __mul__(self, other):
        """
        Returns the multiplication (*) of two Rational numbers.
        """
        properNumerator = self.numerator * other.numerator
        properDenominator = self.denominator * other.denominator

        commonDivisor = gcd(properNumerator, properDenominator)
        properNumerator = int(properNumerator / commonDivisor)
        properDenominator = int(properDenominator / commonDivisor)

        return Rational(properNumerator, properDenominator)

    def __sub__(self, other):
        """
        Returns self minus (-) other of two Rational numbers.
        """
        numerator1 = self.numerator
        denominator1 = self.denominator
        numerator2 = other.numerator
        denominator2 = other.denominator

        commonMultiple = lcm(denominator1, denominator2)
        multiplier1 = int(commonMultiple / denominator1)
        multiplier2 = int(commonMultiple / denominator2)

        return Rational(numerator1 * multiplier1 - numerator2 * multiplier2, commonMultiple)

    def __truediv__(self, other):
        """
        Returns self divided by (/) other.
        """
        # TODO implement this method.
        return self.__mul__(Rational(other.denominator, other.numerator))


def test_rational():
    """
    Put your own tests here.
    This function will never be called during marking.
    """
    print(Rational(2) - Rational(1))
