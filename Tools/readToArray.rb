# Public: Creates a list of words from a file.
#
# dictfile - The .txt file of words (one per line) that will be made into an array.
#
# Returns an array of words from the file all downcased.
def readToArray(file)
  wordList = Array.new
  
  workFile = File.open(file, "r")
  workFile.each_line { |line|
    wordList.push(line.downcase)}
  workFile.close

  return wordList
end