def autobiographical(num):
    if len(str(num)) > 10:
        return False

    digitCount = {"0": 0, "1": 0, "2": 0, "3": 0,
                  "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    for digit in str(num):
        digitCount[digit] += 1

    for i, digit in enumerate([char for char in str(num)]):
        if digitCount[str(i)] != int(digit):
            return False
    return True


num = input("Number: ")

if autobiographical(num):
    print(num, "is autobiographical.")
else:
    print(num, "is not autobiographical.")
