# ALPHASORT --- Sorting My Word List for me
#
# This program takes a word file (one per line) and outputs an alphabetized array for the dictionary
# NOTE: For some reason doesn't make all the words downcase??? Need to fix this...


# INTIALIZNG ARRAY & COUNTER
wordList = Array.new
n = 0

# OPENING THE WORD FILE
file='wordsdict.txt'     
f = File.open(file, "r")
f.each_line { |line|
  wordList.insert(n, line)
  n += 1
  }
f.close

# STORING ALPHABETIZED LIST
alphaList = wordList.sort_by{|word| word.downcase}

# PRINTING OUTPUT TO TEST OR COPYPASTE
puts alphaList

fname = "alphadict.txt"
somefile = File.open(fname, "w")
somefile.puts alphaList
somefile.close


#OUTS PUT A FILE
#fname = "sample.txt"
#somefile = File.open(fname, "w")
#somefile.puts "Hello file!"
#somefile.close



=begin HELPFUL EXAMPLES
# ALPHABETIZES WORD LIST FROM USER INPUT

puts "Type as many words as you like (one per line) to sort alphabetically. Hit Enter when you are finished to receive the output."
wordlist = Array.new
while (userInput = gets.chomp) != ' '
  wordlist.push(userInput)
end
puts wordlist.sort_by{|word| word.downcase}

# READING EVERY LINE IN A TEXT FILE

# Create array
# alphaList = Array.new
# n = 0

file='wordsdict.txt'
f = File.open(file, "r")
f.each_line { |line|
  puts line

# Put each line into a single element
# alphaList.insert(n, line)
  #n += 1
  }
f.close

# puts alphaList

=end