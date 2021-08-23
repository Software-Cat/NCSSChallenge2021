from typing import Dict, List

# Constants
VARIABLE_NAME = "x"

SYMBOLS = {
    "addition": "+",
    "subtraction": "-",
    "multiplication": "*",
    "exponentiation": "^"
}


class Polynomial:

    def __init__(self, degreesAndCoefficients: Dict[int, int]) -> None:
        """Initialize a univariable polynomail

        Args:
            degreesAndCoefficients (Dict[int, int]): e.g. {2: 1, 1: 2, 0: 3} == x^2 + 2x + 3
        """
        self.degreesAndCoefficients = degreesAndCoefficients

    def __repr__(self) -> str:
        string: str = ""

        for degree in reversed(sorted(list(self.degreesAndCoefficients.keys()))):
            # Add coefficient
            coefficient = self.degreesAndCoefficients[degree]
            if coefficient > 1:
                string += SYMBOLS["addition"] + \
                    str(self.degreesAndCoefficients[degree])
            elif coefficient == 1:
                string += SYMBOLS["addition"]
            elif coefficient == 0:
                string += str(self.degreesAndCoefficients[degree])
            elif coefficient == -1:
                string += SYMBOLS["subtraction"]
            else:
                string += str(self.degreesAndCoefficients[degree])

            # Add degree
            if degree > 1:
                string += VARIABLE_NAME
                string += SYMBOLS["exponentiation"] + str(degree)
            elif degree == 1:
                string += VARIABLE_NAME
            elif degree == 0 and (coefficient == 1 or coefficient == -1):
                string += str(abs(coefficient))

            # Space between terms
            string += " "

        # Remove addition symbol at leftmost term
        string = string.lstrip(SYMBOLS["addition"])

        # Add space after symbols
        string = string.replace(
            SYMBOLS["addition"],
            SYMBOLS["addition"] + " ")
        string = string.replace(
            SYMBOLS["subtraction"],
            SYMBOLS["subtraction"] + " ")

        # Fix weird zero
        if len(string) == 0:
            string = "0"

        # Re-correct leftmost symbol
        if string[0] == SYMBOLS["subtraction"]:
            string = string.lstrip(SYMBOLS["subtraction"] + " ")
            string = SYMBOLS["subtraction"] + string

        # Remove trailing spaces
        string = string.rstrip(" ")

        return string

    def copy(self) -> "Polynomial":
        return Polynomial(self.degreesAndCoefficients)

    @staticmethod
    def add(augend: "Polynomial", addend: "Polynomial") -> "Polynomial":
        augend = augend.copy()
        addend = addend.copy()

        for degree in addend.degreesAndCoefficients.keys():
            if degree in augend.degreesAndCoefficients:
                augend.degreesAndCoefficients[degree] += addend.degreesAndCoefficients[degree]
            else:
                augend.degreesAndCoefficients[degree] = addend.degreesAndCoefficients[degree]

        return Polynomial.cleanup(augend)

    @staticmethod
    def subtract(minuend: "Polynomial", subtrahend: "Polynomial") -> "Polynomial":
        minuend = minuend.copy()
        subtrahend = subtrahend.copy()

        for degree in subtrahend.degreesAndCoefficients.keys():
            if degree in minuend.degreesAndCoefficients:
                minuend.degreesAndCoefficients[degree] -= subtrahend.degreesAndCoefficients[degree]
            else:
                minuend.degreesAndCoefficients[degree] = - \
                    subtrahend.degreesAndCoefficients[degree]

        return Polynomial.cleanup(minuend)

    @staticmethod
    def multiply(multiplicand: "Polynomial", multiplier: "Polynomial") -> "Polynomial":
        terms: List[Polynomial] = list()

        # FOIL expand out
        for key1 in multiplicand.degreesAndCoefficients:
            for key2 in multiplier.degreesAndCoefficients:
                addedDegrees = key1 + key2
                multipliedCoefficients = multiplicand.degreesAndCoefficients[key1] * \
                    multiplier.degreesAndCoefficients[key2]

                terms.append(Polynomial(
                    {addedDegrees: multipliedCoefficients}))

        # COllect like terms
        polynomial: Polynomial = Polynomial({})
        for term in terms:
            polynomial = Polynomial.add(polynomial, term)

        return Polynomial.cleanup(polynomial)

    @staticmethod
    def exponent(base: "Polynomial", exponent: "Polynomial") -> "Polynomial":
        base = base.copy()
        polynomial: Polynomial = Polynomial({0: 1})

        for i in range(exponent.degreesAndCoefficients[0]):
            polynomial = Polynomial.multiply(polynomial, base)

        return Polynomial.cleanup(polynomial)

    @staticmethod
    def cleanup(polynomial: "Polynomial") -> "Polynomial":
        polynomial = polynomial.copy()

        keysToRemove: List[int] = list()

        # Audit 0 coefficients for removal
        for degree in polynomial.degreesAndCoefficients.keys():
            if polynomial.degreesAndCoefficients[degree] == 0:
                keysToRemove.append(degree)

        # Perform removal
        for key in keysToRemove:
            del polynomial.degreesAndCoefficients[key]

        return polynomial


def get_unknown_variable(rpn: str) -> str:
    # Tokenize
    tokens: List[str] = rpn.split(" ")

    noIntegers = [x for x in tokens if not (
        x.isdigit() or x[0] == '-' and x[1:].isdigit())]

    noSymbols = [x for x in noIntegers if not x in SYMBOLS.values()]

    if len(noSymbols) > 0:
        return noSymbols[0]
    else:
        return ""


def is_int(s: str) -> bool:
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def parse_rpn(rpn: str) -> Polynomial:
    # Initialize variables
    tokens: List[str] = rpn.split(" ")
    stack: List[Polynomial] = list()

    # Parse through tokens
    for token in tokens:
        if is_int(token):
            stack.append(Polynomial({0: int(token)}))
        elif token is VARIABLE_NAME:
            stack.append(Polynomial({1: 1}))
        elif token in SYMBOLS.values():
            if token is SYMBOLS["addition"]:
                stack.append(Polynomial.add(stack.pop(-2), stack.pop()))
            elif token is SYMBOLS["subtraction"]:
                stack.append(Polynomial.subtract(stack.pop(-2), stack.pop()))
            elif token is SYMBOLS["multiplication"]:
                stack.append(Polynomial.multiply(stack.pop(-2), stack.pop()))
            elif token is SYMBOLS["exponentiation"]:
                stack.append(Polynomial.exponent(stack.pop(-2), stack.pop()))

    return stack[0]


RPN = input("RPN: ")
VARIABLE_NAME = get_unknown_variable(RPN)
print(parse_rpn(RPN))
