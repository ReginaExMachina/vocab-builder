#Public: Program to create a dictionary file for W3 app.
#
# rawDict.txt -  .txt file of words (one per line) in the same directory
# readToArray - Reads a .txt file and returns an array
# removeDups - Removes duplicates from an array and returns a copy.
# alphaSort - Alphabetizes an array
#
# Returns a new .txt file (dict.txt) with each word from the original file alphabetized. Original rawDict.txt file remains intact.

#Main Program
begin 
  require 'readToArray.rb'
  require 'removeDups.rb'
  require 'alphaSort.rb'

  #Makes sure required input file exists
  if File.exist?("rawDict.txt")
      endGame = alphaSort(removeDups(readToArray("rawDict.txt")))
  else
    print "An error has occured. Please make sure there is file named rawDict.txt in the same directory as this program."
  end
  
  #Creating final file
  newDict = "dict.txt"
  
  newfile = File.open(newDict, "w")
  newfile.puts endGame
  newfile.closes
  
  print "New dictionary file created. Bye!"

#Ends Program if required methods are missing
rescue ScriptError
  print 'An error has occurred. Please make sure the required files are in the same directory as this program.'
end