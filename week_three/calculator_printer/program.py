# Each bool in a digit represents 1 segment,
# going clockwise starting from top horizontal bar.
# Ending at middle segment.

def get_digit_list(digit, size):
    digitGrid = []
    for i in range(size * 2 + 3):
        digitGrid.append([" " for j in range(size + 2)])

    width = len(digitGrid)
    length = len(digitGrid[0])

    if DIGITS[digit][0]:
        for i in range(1, length - 1):
            digitGrid[0][i] = "-"
    if DIGITS[digit][1]:
        for i in range(1, size + 1):
            digitGrid[i][-1] = "|"
    if DIGITS[digit][2]:
        for i in range(size + 2, width - 1):
            digitGrid[i][-1] = "|"
    if DIGITS[digit][3]:
        for i in range(1, length - 1):
            digitGrid[-1][i] = "-"
    if DIGITS[digit][4]:
        for i in range(1, size + 1):
            digitGrid[i][0] = "|"
    if DIGITS[digit][5]:
        for i in range(size + 2, width - 1):
            digitGrid[i][0] = "|"
    if DIGITS[digit][6]:
        for i in range(1, length - 1):
            digitGrid[size + 1][i] = "-"

    return digitGrid


DIGITS = [
    [True, True, True, True, True, True, False],
    [False, True, True, False, False, False, False],
    [True, True, False, True, False, True, True],
    [True, True, True, True, False, False, True],
    [False, True, True, False, True, False, True],
    [True, False, True, True, True, False, True],
    [True, False, True, True, True, True, True],
    [True, True, True, False, False, False, False],
    [True, True, True, True, True, True, True],
    [True, True, True, True, True, False, True],
]

number = input("Number: ")
size = int(input("Width: "))

grid = []
for i in range(size * 2 + 3):
    grid.append([" " for j in range((size + 3) * len(number) - 1)])

for i, digit in enumerate(number):
    offset = i * (size + 3)

    digitList = get_digit_list(int(digit), size)
    for j, row in enumerate(digitList):
        for k, char in enumerate(row):
            grid[j][k + offset] = char

for row in grid:
    for char in row:
        print(char, end="")
    print()
