import random


class MarkovModel:
    def __init__(self):
        self.bigrams = {}

    def fit(self, fileDir):
        # Split file into tokens
        tokens = []
        with open(fileDir, "r") as file:
            tokens = file.read().replace("\n", " ").lower().split(" ")
            tokens = [token for token in tokens if token !=
                      "" and token != " "]

        # Store tokens in model
        for i in range(len(tokens) - 1):
            if not tokens[i] in self.bigrams:
                self.bigrams[tokens[i]] = []
            self.bigrams[tokens[i]].append(tokens[i+1])

    def predict_next(self, token):
        if not token in self.bigrams:
            raise ValueError("There is no next possible token.")
        return random.choice(self.bigrams[token])


def get_full_path(shortPath):
    return "./week_two/markov_text_generator/" + shortPath


def generate_sentence(startToken, learnFiles):
    model = MarkovModel()

    for file in learnFiles:
        model.fit(file)

    generatedTokens = [startToken.lower()]

    while len(generatedTokens) < 200:
        try:
            generatedTokens.append(model.predict_next(generatedTokens[-1]))
        except ValueError:
            break
        if generatedTokens[-1] == ".":
            break

    return " ".join(generatedTokens).strip(" ")


if __name__ == '__main__':
    # The random number generator is initialised to zero here purely
    # for your own testing so that each time you run your code during
    # development, you will get the same output. Remove this to get
    # different output each time you run your code with the same input.
    random.seed(0)

    # Run the examples in the question.
    for i in range(4):
        print(generate_sentence('There', [get_full_path('single.txt')]))
    print('=' * 80)
    for i in range(4):
        print(generate_sentence('the', [get_full_path('jab.txt')]))
    print('=' * 80)
    for i in range(4):
        print(generate_sentence('It', [get_full_path(
            'dracula.txt'), get_full_path('pandp.txt')]))
    print('=' * 80)
    for i in range(10):
        print(generate_sentence(
            'Once', [get_full_path('dracula.txt'), get_full_path('jb.txt'), get_full_path('pandp.txt'), get_full_path('totc.txt')]))
    print('=' * 80)
    for i in range(8):
        print(generate_sentence('cat', [get_full_path(
            'single.txt'), get_full_path('textwraps.txt')]))
    print('=' * 80)
    for i in range(10):
        print(generate_sentence(
            'Once', [get_full_path('dracula.txt'), get_full_path('jb.txt'), get_full_path('pandp.txt'), get_full_path('totc.txt')]))
