import random
words = ["apple", "banana", "computer", "python","codealphaa"]
secret = random.choice(words)
guessed = set()
wrong_guesses = 0
max_wrong = 6

hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

def display_word(secret, guessed):
    return " ".join([c if c in guessed else "_" for c in secret])

print("Welcome to Hangman!")

while True:
    print(hangman_stages[wrong_guesses])
    print("Word:", display_word(secret, guessed))
    print("Guessed:", " ".join(sorted(guessed)))
    guess = input("Enter a letter (or 'quit'): ").lower().strip()

    if guess == "quit":
        print("Goodbye! The word was:", secret)
        break

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed", guess)
        continue

    guessed.add(guess)

    if guess not in secret:
        wrong_guesses += 1
        print("Wrong!")
        if wrong_guesses >= max_wrong:
            print(hangman_stages[wrong_guesses])
            print("You lost! The word was:", secret)
            break
    else:
        print("Good guess!")
        if all(c in guessed for c in secret):
            print("You won! The word was:", secret)
            break
