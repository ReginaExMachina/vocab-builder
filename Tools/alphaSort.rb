# Public: Alphabetizes an array 
#
# nonAlphalist - The .txt file of words (one per line) or array to have its duplicates removed.
#
# Returns a copy of the array alphabetized.
def alphaSort(nonAlphalist)
  alphaList = nonAlphalist.sort_by {|word| word.downcase}
  return alphaList
end
