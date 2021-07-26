
def to_camel(ident):
    if ident == "":
        return ""

    tokens = ident.split('_')

    _camelTokens = []
    for i, token in enumerate(tokens):
        if(i != 0):
            _camelTokens.append(token.upper()[0] + token[1:])
        else:
            _camelTokens.append(token.lower()[0] + token[1:])

    return ''.join(_camelTokens)


if __name__ == '__main__':
    # Run the example inputs in the question.
    print(to_camel('foo'))
    print(to_camel('raw_input'))
    print(to_camel('num2words'))
    print(to_camel('num_to_SMS'))
