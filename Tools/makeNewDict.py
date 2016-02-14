#!/usr/bin/env python

def askforAppend(file):
    # file: A .txt file with a string on each line. Also works with lists.
    #       Program assumes that each string is a single word.
    # Outputs a list of each word confirmed by user.
    
    dictList = []
    
    for line in file:
        print("Word is : "),
        print(line)
        answer = raw_input("Would you like to add it to the dictionary? Y or N: ")
        if answer.lower() == "y" or answer.lower() == "yes":
            dictList.append(line.lower())
        #else:
        #    aMistakeMade = raw_input("Start over? Y or N: ")
        #    if aMistakeMade == "Y":
        #        askforAppend(file)
        file.close()
    return dictList

def makeNewDict(dictList):
    newFile = open("dict.txt", "w")
    for n in dictList:
        newFile.writelines(n)
    newFile.close()
