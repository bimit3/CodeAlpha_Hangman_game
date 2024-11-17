import random

def play_hangman():
    word_list = ["python", "hangman", "programming", "code", "algorithm"]
    secret_word = random.choice(word_list).upper()
    current_guess = ["_"] * len(secret_word)
    guessed_letters = set()
    remaining_attempts = 6

    print("Welcome to Hangman!")
    print(" ".join(current_guess))

    while remaining_attempts > 0 and "_" in current_guess:
        player_input = input("\nGuess a letter: ").upper()

        if len(player_input) != 1 or not player_input.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if player_input in guessed_letters:
            print(f"You already guessed '{player_input}'.")
            continue

        guessed_letters.add(player_input)

        if player_input in secret_word:
            for index, letter in enumerate(secret_word):
                if letter == player_input:
                    current_guess[index] = player_input
            print(f"Correct! '{player_input}' is in the word.")
        else:
            remaining_attempts -= 1
            print(f"Wrong guess! You have {remaining_attempts} attempts left.")

        print(" ".join(current_guess))

    if "_" not in current_guess:
        print("\nCongratulations! You've guessed the word correctly.")
    else:
        print(f"\nGame Over! The word was '{secret_word}'.")

play_hangman()
