def propagate_interleaving(str1, str2, interleavingStr, len1, len2, depth):
    if len1 == 0 and len2 == 0:
        possibilities.append("".join(interleavingStr))

    if len1 != 0:
        interleavingStr[depth] = str1[0]
        propagate_interleaving(
            str1[1:], str2, interleavingStr, len1-1, len2, depth+1)

    if len2 != 0:
        interleavingStr[depth] = str2[0]
        propagate_interleaving(
            str1, str2[1:], interleavingStr, len1, len2-1, depth+1)


def interleavings(str1, str2):
    # Variable declaration
    interleavingStr = [''] * (len(str1) + len(str2))
    global possibilities
    possibilities = []

    # Calculate all possible interleavings
    propagate_interleaving(str1, str2, interleavingStr,
                           len(str1), len(str2), 0)

    return sorted(possibilities)


if __name__ == '__main__':
    # Run the examples in the question.
    result = interleavings('ab', 'cd')
    print(result)
    result = interleavings('a', 'cd')
    print(result)
