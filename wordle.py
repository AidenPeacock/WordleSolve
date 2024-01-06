import random

# Read list of words from the file into a list
def read_words(filename):
    file = open(filename, "r")
    words = file.readlines()
    file.close()
    return words

def select_word(words):
    word = random.choice(words).strip()
    return word

def run_game(answer):
    guesses = 0
    feedback = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]

    # x = letter not in word, ? = letter not in right place, ! = right letter in right place

    while guesses < 6:
        print("You have " + str(6 - guesses) + " guesses left.")
        guess = input("Guess #" + str(guesses + 1) + ": ")
        if guess == answer:
            print("Nice")
            break

        i = 0
        while i < 5:
            if guess[i] == answer[i]:
                feedback[guesses][i] = "!"
            elif guess[i] in answer:
                feedback[guesses][i] = "?"
            else:
                feedback[guesses][i] = "x"
            i += 1
        
        print(feedback[guesses])
        guesses += 1
    
    print("The word was " + answer)


# Test
words = read_words("answerlist.txt")
answer = select_word(words)
run_game(answer)


        
