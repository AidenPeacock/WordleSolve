
import numpy as np
import random
import re
import math

import time

legalGuesses = []
legalWords = []



f = open("answerlist.txt", "r")
for line in f:
    legalWords.append(line.strip())
f.close()
f = open("wordle_possibles.txt", "r")
for line in f:
    legalGuesses.append(line.strip())
f.close()


def RegBuild(word, information, legalwords):
    blkletter = ""
    ylpre = ""
    grnre = ""
    newerlist = []
    newlist = []
    for it in range(len(information)):
        if information[it] == "b":
            blkletter += word[it]
        if information[it] == "y":
            ylpre += "[^" + word[it] + "]"
            for check in legalwords:
                if re.search("[" + word[it] + "]", check):
                    newerlist.append(check)
            newlist = newerlist
            newerlist = []
            legalwords = newlist
        else:
            ylpre += "[a-z]"
        if information[it] == "g":
            grnre += "[" + word[it] + "]"
        else:
            grnre += "[a-z]"
    blackre = "[^"
    builder = ""
    for letter in blkletter:
        builder += letter
    if blkletter != "":
        blackre = (blackre + builder + "]")*5
    else:
        blackre = "[a-z]"*5
    for word in legalwords:
        if re.search(blackre, word):
            newerlist.append(word)
    legalwords = newerlist
    newerlist = []
    if grnre != "":
        for word in legalwords:
            if re.search(grnre, word):
                newerlist.append(word)
    legalwords = newerlist
    newerlist = []
    for word in legalwords:
        if re.search(ylpre, word):
            newerlist.append(word)
    return newerlist
def SafeLog(val):
    return math.log2(val) if val > 0 else 0

def ExpectedInformation(word, legalwords):
    summate = 0
    for sp1 in ["b", 'y', 'g']:
        for sp2 in ["b", 'y', 'g']:
            for sp3 in ["b", 'y', 'g']:
                for sp4 in ["b", 'y', 'g']:
                    for sp5 in ["b", 'y', 'g']:
                        string = sp1+sp2+sp3+sp4+sp5
                        parsed = RegBuild(word, string, legalwords)
                        summate += -SafeLog(len(parsed)/len(legalwords))*(len(parsed)/len(legalwords))
    return summate


it = 0
maximum = 0
maxword = ""


summate = ExpectedInformation("raise", legalWords)

print(RegBuild("apple", "ggbbb", legalWords))

