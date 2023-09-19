from random import *

player_score = 0
computer_score = 0

hang_man = {1:'''
  +---+
  |   |
      |
      |
      |
      |
=========''',2:'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',3:'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',4:'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',5:'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',6:'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',7:'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''}

def guess_letter():
    letter = input("\nGuess a letter in the animal's name: ").strip().lower()
    return letter

def scores():
    global player_score, computer_score
    print(f"High Scores \nPlayer: {player_score} \nComputer: {computer_score}")

def play_again():
    answer = input("Would you like to play again? y/n ").strip().lower()
    if answer == "y":
        return answer
    else:
        print("\nThanks for playing!")

def start():
    print("Lets Start the Game of Animal Hangman")
    while game():
        pass
    scores()

def game():
    word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split() # can add .split to this dictionary to turn the words into individual objects in a list

    word = choice(word_list) #random import . choice choose item from list

    word_length = len(word)
    clue = word_length * ["_"]
    tries = 8
    letters_tried = ""

    letters_wrong = 0
    global computer_score, player_score

    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha(): #isalpha() tests to see if all the characters are letters,
                                                  # conditional sees if there is one element of an alphabet
            if letters_tried.find(letter) != -1: #.find locates the position of the letter, checks to see if the letter was already used
                                                 # if the letter was already used it can't equal -1, so then the statement is printed
                print("\nLetter already tried"), letter
            else:
                letters_tried = letters_tried + letter #adds letter to a list of letters that were already used
                first_index = word.find(letter) #locates the position of the letter in the word
                if first_index == -1:
                    letters_wrong += 1
                    print(f"\nSorry {letter} is not in this word")
                else:
                    print(f"\nCongratulations {letter} is in the word")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("\nThis is not a single letter, please enter again")

        print(f"Gusses Left: {tries - letters_wrong}")

        if 0 < letters_wrong < tries:
            print(hang_man[letters_wrong])

        print(" ".join(clue))
        print(f"Letters Guessed: {letters_tried}")

        if letters_wrong == tries:
            print(f"\nGame over! \nThe word was: {word}")
            computer_score += 1
            break

        if "".join(clue) == word:
            print(f"\nYou win! \nThe word was: {word}")
            player_score += 1
            break

    return play_again()

if __name__ == "__main__":
    start()





