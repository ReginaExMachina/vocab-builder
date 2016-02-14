#!/usr/bin/env python

# CREATING FUNCTIONS
def makeDisplay(l, start, end):
    if end > len(l):
        end = len(l) + 1
    
    newList = l[start:end]
    
    # Testing newList creation, remove for final program
    #print(newList)
    # Clearscreen function should go here
    
    for n in newList:
        print(str(newList.index(n)) + ". " + n),
        if newList.index(n) % 4 == 0 and newList.index(n) != 0:
            print(" ")
    print(" ")
 

def manageInput(userInput):
    # Makes sure that userInput is a string, then returns the first letter of userInput lowercase
    # This makes sure to cover a variety of user input by making assumptions about their intentions.
    # IE. If user accidentally types 'yES', the program will take it in as 'y' and will run with that.
    # Might be better to only lowercase each input for global use.
    if type(userInput) != str:
        print("Please enter a command.")
    return userInput[0].lower()
     
    
# SAMPLE LIST
impList = ["Alice", "tEa", "white rabbit", "Red Queen", "Jaberwocky", "Mad Hatter", "March hare", "Dormouse", "White Knight", "Chesire caT"]


# INTIALIZING VARIABLES
dictList = []

# For main loop
done = False

# Making sure the Stages Work
addStage = False
deleteStage = False
editStage = False
selectStage = True


# MAIN PROGRAM------------------------------------------------------------------

# ACTUAL PROGRAM LINE
#file = open('alphaList', 'r')

#TESTING FOR TUTOR LINE
file = impList

# Creates Dictionary List from File
for line in file:
    dictList.append(line.lower())


# Start Main Loop
while done == False:
    startIndex = int(raw_input("Start from?" ))
    endIndex = int(raw_input("Stop before?" ))
    
    makeDisplay(dictList, startIndex, endIndex)
    
    # Enters Desired Stage (Add, Delete, Edit)
    while selectStage == True:
        stage = manageInput(raw_input("Add, Delete or Edit? Press R to Reset the Display or X to Exit Program. "))
        if stage == "d":
            deleteStage = True
            break
        elif stage == "a":
            addStage = True
            break
        elif stage == "e":
            editStage = True
            break
        elif stage == "r":
            selectStage == False
            break
        elif stage == "x":
            selectStage == False
            break
    
    while addStage == True:
        print("Addition Stage. Enter X to Exit....")
        try:
            wordToAdd = raw_input("What word would you like to add? ")
            if wordToAdd == "x":
                addStage = False
                break
            else:
                if wordToAdd in dictList:
                    print(wordToAdd + " is already in dictionary.")
                dictList.append(wordToAdd.lower())
        except ValueError:
                print("Please enter a word... ")
                
    while deleteStage == True:
        print("Deletion Stage. Enter X to Exit....")
        try:
            wordToDelete = raw_input("Which word would you like to delete which word? ")
            if wordToDelete == "x":
                deleteStage = False
                break
            else:
                dictList.remove(wordToDelete)
        except ValueError:
            print("Please decide properly..." )
     
    # Edits Words        
    while editStage == True:
        print("Editing Stage. Enter X to Exit.... ")
        try:
            wordToEdit = raw_input("Which word would you like to edit? ")
            if wordToEdit.lower() == "x" or wordToEdit.lower() == "exit":
                editStage = False
                break
            else:
                indexForEdit = dictList.index(wordToEdit)
                editedWord = str(raw_input("Word is  : " + wordToEdit + " Change to.... "))
                if editedWord.lower() == "x" or editedWord.lower() == "exit":
                    break
                dictList.remove(wordToEdit)
                dictList.insert(indexForEdit, editedWord)
        except ValueError:
            print("Please pick a word from the list... ")
            
    
    answer = manageInput(raw_input("Press X to make final list or press anything to keep working... " ))
    if answer == "x":
        done = True
        # Exits main program loop
    else:
        selectStage == True


# OUTPUTS Edited list into file 
#ACTUAL PROGRAM LINE
#name = str(raw_input("Please name your new file: "))
#name = name + ".txt"

## Creates new file, writes list
#newFile = open(name, "w")
#for n in dictList:
#    newFile.writelines(n)
#newFile.close()

#TEST LINE
print(dictList)


# End of Program
print("All done, bye!")
