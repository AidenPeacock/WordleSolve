import random

# Read list of words from the file into a set
def read_words(filename):
    file = open(filename, "r")
    words = file.readlines()
    # Remove newline character from each word
    words = set(map(lambda s : s.strip(), words))
    file.close()
    return words

# Select a random word from a set of words
def select_word(words):
    word = random.choice(list(words))
    return word


def run_game(answer, validWords):
    guesses = 0
    feedback = ["", "", "", "", ""]

    print("Welcome to Wordle! You have 6 guesses to guess a 5-letter word.")
    print("x = letter is not in the word, ? = letter is in the word but in the wrong place, ! = letter is correct and in right place.")
    print("Enter \"quit\" at any time to concede.")

    while guesses < 6:
        print("You have " + str(6 - guesses) + " guesses left.")

        # Ensure user enters a valid word
        while True:             
            guess = input("Guess #" + str(guesses + 1) + ": ").lower()
            if (guess in validWords) or (guess == "quit"):
                break
            print("Not a valid word. Try Again.")
        
        if guess == "quit":
            break

        if guess == answer:
            print("Nice!")
            break

        # Keep track of letters in the answer that have and have not been guessed correctly
        lettersLeft = {}
        for letter in answer:
            if lettersLeft.get(letter) == None:
                lettersLeft[letter] = 1
            else:
                lettersLeft[letter] += 1

        i = 0
        while i < 5:
            if guess[i] == answer[i]:
                feedback[i] = "!"
                lettersLeft[guess[i]] -= 1
            elif (lettersLeft.get(guess[i]) != None) and (lettersLeft.get(guess[i]) != 0):
                feedback[i] = "?"
                lettersLeft[guess[i]] -= 1
            else:
                feedback[i] = "x"
            i += 1
        

        # hack to fix bug (ex: guessing harsh when answer is flush had the first letter be ? and not x)
        i = 0
        while i < 5:
            if (lettersLeft.get(guess[i]) != None) and (lettersLeft.get(guess[i]) < 0):
                feedback[i] = "x"
                lettersLeft[guess[i]] += 1
            i += 1

        print(str(feedback))
        guesses += 1
    
    print("The word was " + answer)


if __name__ == "__main__":
    words = read_words("answerlist.txt")
    validWords = read_words("valid-wordle-words.txt")
    answer = select_word(words)
    run_game(answer, validWords)
