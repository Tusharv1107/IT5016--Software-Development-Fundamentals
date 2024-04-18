import random

# List of words for the game
words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon', 'pineapple']

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

# Function to play the game
def hangman():
    # Choose a random word
    word = choose_word()
    # Set up variables
    guessed_letters = []
    attempts = 6
    print ("\n------------------")
    print("Welcome to Hangman!")
    print ("\n------------------")
    print(" \n***********Try to guess the word**************")

    while attempts > 0:
        # Display the current state of the word
        print(display_word(word, guessed_letters))
        
        # Display the number of attempts left
        print("\nAttempts left:", attempts)
        
        # Ask the user for a guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess not in word:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Correct guess!")
            

        # Check if the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print ("\n***************************************")
            print("\nCongratulations! You guessed the word:", word)
            print ("\n***************************************")
            break

    else:
        print("\nSorry, you've run out of attempts. The word was:", word)

# Play the game
hangman()