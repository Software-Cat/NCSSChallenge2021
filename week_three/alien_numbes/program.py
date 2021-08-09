def is_valid(string):
    # Improper formatting test
    if len(string) > 1:
        for i in range(1, len(string)):
            if string[i - 1] == "a" or string[i - 1] == "e" or string[i - 1] == "i" or string[i - 1] == "o" or string[i - 1] == "u":
                lastCharCase = "LOWER"
            else:
                lastCharCase = "UPPER"
            if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
                thisCharCase = "LOWER"
            else:
                thisCharCase = "UPPER"
            
            if lastCharCase == "LOWER" and thisCharCase == "UPPER":
                return False
    return True

quinaryLookup = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}

def alien2float(quinaryString):
    try:
        if not is_valid(quinaryString):
            return None
        
        decimalPlaces = 0
        for char in quinaryString:
            if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                decimalPlaces += 1
        
        total = 0
        for char in reversed(quinaryString):
            digit = quinaryLookup[char.lower()]
            total += digit * (5**(-decimalPlaces))
            decimalPlaces -= 1
        
        return float(total)
    except Exception:
        return None


if __name__ == "__main__":
    # Run the examples in the question.
    print(repr(alien2float("IUae")))
    print(repr(alien2float("OUAooea")))
    print(repr(alien2float("iuAE")))
    print(repr(alien2float("E")))