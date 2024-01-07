import random

# Read set of words from the file into a list
def read_words(filename):
    file = open(filename, "r")
    words = file.readlines()
    # Remove newline character from each word
    words = set(map(lambda s : s.strip(), words))
    file.close()
    return words

def select_word(words):
    word = random.choice(list(words))
    return word

def run_game(answer, validWords):
    guesses = 0
    feedback = ["", "", "", "", ""]

    # x = letter not in word, ? = letter not in right place, ! = right letter in right place

    while guesses < 6:
        print("You have " + str(6 - guesses) + " guesses left.")

        guess = input("Guess #" + str(guesses + 1) + ": ").lower()
        while guess not in validWords:
            print("Not a valid word. Try Again.")
            guess = input("Guess #" + str(guesses + 1) + ": ").lower()
        if guess == answer:
            print("Nice")
            break

        letterCounts = {}
        for letter in answer:
            if letterCounts.get(letter) == None:
                letterCounts[letter] = 1
            else:
                letterCounts[letter] += 1


        i = 0
        while i < 5:
            if guess[i] == answer[i]:
                feedback[i] = "!"
                letterCounts[guess[i]] -= 1
            elif (letterCounts.get(guess[i]) != None) & (letterCounts.get(guess[i]) != 0):
                feedback[i] = "?"
                letterCounts[guess[i]] -= 1
            else:
                feedback[i] = "x"
            i += 1
        

        print(str(feedback))
        guesses += 1
    
    print("The word was " + answer)


if __name__ == "__main__":
    words = read_words("answerlist.txt")
    validWords = read_words("valid-wordle-words.txt")
    answer = select_word(words)
    run_game(answer, validWords)
