from pickle import FALSE, TRUE
# from colorama import init, Fore, Back, Style
import random

# reads the word list
def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

def goodLetters(letters, words):
    good_letters = list(letters)
    good_words = []
    for word in words:
        if all([char in word for char in good_letters]):
            good_words.append(word)
    return good_words

def goodPos(letter_pos, good_words):
    great_words = []
    letter_pos = list(letter_pos)
    for word in good_words:
       for char, i in zip(letter_pos, range(0,5,1)):
        if char == " ":
            if i == 4:
                great_words.append(word)
            continue
        if char != word[i]:
            break
        if i == 4:
            great_words.append(word)
    return great_words

def badLetters(bad_letters, good_words):
    bad_letters = list(bad_letters)
    bad_words = []
    for word in good_words:
        for char in bad_letters:
            if char in word:
                bad_words.append(word)
    return bad_words

def badPos(bad_pos, good_words):
    bad_words = []
    for key, i in zip(bad_pos, range(0, 5, 1)):
        letters = bad_pos.get(key)
        if letters == None:
            continue
        for letter in letters:
            for word in good_words:
                if letter in word[i]:
                    bad_words.append(word)
    return bad_words

def removeCommon(bad_words, good_words):
    for i in bad_words[:]:
        if i in good_words:
            good_words.remove(i)
    return good_words

def noDup(non_dup, good_words):
    bad_words = []
    for dup in non_dup:
        for word in good_words:
            i = 0
            for char in word:
                #print("hello", i, dup, char)
                if char == dup:
                    i += 1
                if i > 1:
                    bad_words.append(word)
    return bad_words

def colours(result):
    if all(elem == "green" for elem in result):
        print('success!')
        return TRUE
    
    


def main():
    word_list = readFile("./wordList.txt")
    bad_pos = {1: '', 2: '', 3: '', 4: '', 5: ''}
    good_words = goodLetters("ar", word_list)
    good_words = goodPos("  ar ", good_words)
    bad_words = badLetters("soechtquk", good_words)
    good_words = removeCommon(bad_words, good_words)
    bad_words = badPos(bad_pos, good_words)
    good_words = removeCommon(bad_words, good_words)
    bad_words = noDup("", good_words)
    good_words = removeCommon(bad_words, good_words)

    print(good_words)
    print(good_words[0])

    # for i in range(0,6, 1): 
    #     guess = input("enter your guess\n").split("")
    #     result = input("enter result\n").split("")
    #     if colours(result, guess, goodletters, badletters, bad_pos, goodpositions):
    #         break




if __name__ == "__main__":
    main()