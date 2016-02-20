#!/usr/bin/env python

    # MAKING A FINAL DICTIONARY PROGRAM
    
    # Reads the word list file and then inputs each word lowercased into a new file
    #if user confirms. No exception handling yet...

dictList = []

file = open('alphaList', 'r')

for line in file:
    done = False
    print ("Word is : "),
    print(line)
    while done == False:
        try:
            answer = raw_input("Would you like to add it to the dictionary? Y or N: ")
            if answer.lower() == "y" or answer.lower() == "yes":
                # Puts line into dictList
                dictList.append(line.lower())
                done = True
            elif answer.lower() == "n" or answer.lower() == "no":
                done = True
            else:
                print("Please enter Y or N for " + line + " : ")
        except ValueError:
            print("Please decide properly...")
            
file.close()

# Finishing up

print(dictList)

finish = raw_input("Is this the final list? Y or N: ")
if finish == "Y":
    newFile = open("dict.txt", "w")
    for n in dictList:
        newFile.writelines(n)
# If no, re-run function on created dictList
newFile.close()

print("All done!")
