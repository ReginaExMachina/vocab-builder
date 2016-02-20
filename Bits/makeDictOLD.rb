# Deprecated

wordList = Hash.new

file = 'alphaList.rb'
n = 0

d = File.open(file, "r")
d.each_line { |line|
wordList.store(n, line) 
n += 1 }

d.close

print wordList


## OUTPUTS ---- New dict.txt
#finalDict = "dict.txt"
#endFile = File.open(finalDict, "w")
#endFile.puts wordList
#endFile.close
