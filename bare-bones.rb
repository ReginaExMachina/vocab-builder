#!/usr/bin/env ruby

#Initializing the Words and Definitions Dictionaries
w3Dict = {0 => 'word1', 1 => 'word2', 2 => 'word3'}
w3DictDef = {0 => 'definition1', 1 => 'defintion2', 2 => 'definition3'}

#MAIN FUNCTION - This displays a coupled selection of Words and Defs #randomnly
n = w3Dict.length

#Should clone w3Dicts and add addtional lists for each go
word = rand(n)

puts w3Dict[word]
puts w3DictDef[word]

# As function
def wordDisplay (dict, defins)
  word = rand(dict.length) + 1
  return dict[word] + defins[word]
end

print wordDisplay(w3Dict, w3DictDef)
