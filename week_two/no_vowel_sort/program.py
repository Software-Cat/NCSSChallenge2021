def strip_vowels(string):
    return string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

def novowelsort(list):
    noVowelAndVowelPairs = [(strip_vowels(string), string) for string in list]
    noVowelAndVowelPairs.sort()
    return [pair[1] for pair in noVowelAndVowelPairs]


if __name__ == '__main__':
    # Example calls to your function.
    print(novowelsort(['alpha', 'beta']))
    print(novowelsort(['once', 'upon', 'abc', 'time', 'there', 'were', 'some', 'words']))