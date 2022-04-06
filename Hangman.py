import random
import time
from loading import loading
# Transforming txt file to a list in python using strip()
thousand_random_word = open("words.txt","r")
word_list = []
for line in thousand_random_word:
    split = line.strip()
    word_list.append(split)

# Function 1 to get word
def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Hello, welcome to HANGMAN game!")
    time.sleep(1.5)
    print("Try to find the given secret word!")
    time.sleep(1.5)
    print("Let us create your random word!")
    time.sleep(1)
    loading("Creating")
    print(f"Your word has {len(word)} letters.")
    print(word_completion)
    time.sleep(1)
    print("Now you can start!")
    counter = 0
    while not guessed and tries > 0:
        if counter != 0:
            print("Guessed letters: ", guessed_letters)
        guess = input("Please guess a letter or word: ").upper()
        counter += 1
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter")
            elif guess not in word:
                print("Guess is not in the word.")
                print("You have " + str(tries) + " tries left. Be careful!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job ", guess, " is in the word")
                print("You have " + str(tries) + " tries. Keep going!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed == True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess")
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats you guessed the word! You win!")
    else:
        print("Sorry you ran out of tries. The word was ", word ,". Maybe next time!")

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
main()

