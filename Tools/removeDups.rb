# Public: Removes duplicates from a list of words.
#
# dict - The .txt file of words (one per line) or array to have its duplicates removed.
#
# Examples
#
#   removeDups(["thor", "loki", "thor", "thor"])
#   => ["thor", "loki"]
#
# Returns a copy if the array without duplicates.
def removeDups(dictList)

  finalList = []

  for elem in dictList do
      #Creates finalList without dups
      unless finalList.include?(elem)
        finalList.push(elem)
      end
  end
  
  return finalList

end