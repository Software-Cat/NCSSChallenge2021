from typing import List


digits: List[int] = [int(i) for i in input("Enter number: ")]
validationDigit = digits.pop()

doubledDigits = []
for i, digit in enumerate(digits):
    if i % 2 == 0:
        doubledDigits.append(digit)
    else:
        doubledDigits.append(digit * 2)

digitSum = 0
for digit in doubledDigits:
    if digit < 10:
        digitSum += digit
    else:
        digitSum += int(str(digit)[0])+int(str(digit)[1])

if (digitSum + validationDigit) % 10 == 0:
    print("Valid.")
else:
    print("Invalid.")
