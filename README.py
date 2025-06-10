import random

# Predefined list of words
word_list = ["apple", "tiger", "robot", "house", "candy"]
chosen_word = random.choice(word_list)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

# Create a display version of the word with underscores
display_word = ["_" for _ in chosen_word]

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_incorrect and "_" in display_word:
    print("Word:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct guess!\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! You have {max_incorrect - incorrect_guesses} tries left.\n")

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Game Over! The word was:", chosen_word)
