# Public: Toybox verison of w3 program
#
# w3_dict - dictionary of interesting words.
# w3_defs - dictionary of definitions.
#
# Keys for both dicts are matching integers for word/defintion.
#
# word_display() - Displays a randomly generated word and its definition.
# learning_listed - Removes displayed word from main list.

# Returns a random set of 1: A word from the list and it's definition.


w3_dict = { 
          1: 'amorous',
          2: 'amorphous',
          3: 'antithesis',
          4: 'apostate',
          5: 'apotheosis',
          6: 'belligerent',
          7: 'beneficent',
          8: 'bromide',
          9: 'callipygian',
          10: 'censorious',
          11: 'cistern',
          12: 'codicil',
          13: 'cognizant',
          14: 'cognomen',
          15: 'concise',
          16: 'corollary',
          17: 'debonair'
          }

w3_defs = {
          1: '1: inclined toward or displaying love 2: expressive of or exciting sexual love or romance',
          2: 'formless, shapeless, having no definite form or distinct shape',
          3: '1: exact opposite 2: the juxtaposition of contrasting words or ideas to give a feeling of balance',
          4: '1: a disloyal person who betrays or deserts his cause or religion or political party or friend etc. 2: not faithful to religion or party or cause',
          5: '1: model of excellence or perfection of a kind; one having no equal 2: the elevation of a person ie. as to the status of a god',
          6: 'characteristic of an enemy or one eager to fight',
          7: 'doing or producing good',
          8: '1: any of the salts of hydrobromic acid; formerly used as a sedative but now generally replaced by safer drugs 2: a trite or obvious remark',
          9: 'pertaining to or having finely developed buttocks',
          10: 'harshly critical or expressing censure',
          11: 'an artificial reservoir for storing liquids; especially an underground tank for storing rainwater',
          12: 'a supplement to a will; a testamentary instrument intended to alter an already executed will',
          13: 'having or showing knowledge or understanding or realization or perception',
          14: 'a familiar name for a person',
          15: 'expressing much in few words',
          16: '1: a practical consequence that follows naturally 2: an inference that follows directly from the proof of another proposition',
          17: '1: having a sophisticated charm 2: having a cheerful, lively, and self-confident air' 
          }


from random import randint

# INTIALIZING VARIABLES
n = len(w3_dict) #May switch for randrange
choice = ''

learning_list = {}
learning_list_defs = {}

# MAKING METHODS
def word_display():
    word = randint(1,n)
    #word = random.randrange(0, len(w3_dict))

    print w3_dict[word]
    print w3_defs[word]
    learning_listed(word)

def learning_listed(word):
    new_word = w3_dict.pop(word)
    new_def = w3_defs.pop(word)
    
    learning_list.update({word: new_word})
    learning_list_defs.update({word: new_def})


print("W3")
print('Press E to Exit or any key to reload.\n')

while choice != 'E':
    
    word_display()
    choice = raw_input('\n ')
    print(' ')
