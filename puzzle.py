import random


class Puzzle:
    '''The purpose of this class is to randomly select a word from the word list.
    
    Sterotyope:
        Information Holder

    Attributes:
        word_list (list): a list of words for the puzzle to choose from
        puzzle (string): a random word from the word list
    '''

    def __init__(self):
        '''Class constructor. Declares and initializes instance attributes. 
        
        Args:
            self (Puzzle): An instance of Puzzle.
        '''
        self.word_list = ["teach","applied","remain","back","raise","pleasant"
        "organization","plenty","continued","all","seldom","store"
        "refer","toy","stick","by","shine","field"
        "load","forth","well","mine","catch","complex"
        "useful","camera","teacher","sit","spin","wind"
        "drop","coal","every","friend","throw","wool"
        "daughter","bound","sight","ordinary","inch","pan"] 
    
    def random_word(self):
        '''Gets a random word from the word list. 
        
        Returns: the word
        '''
        self.word = random.choice(self.word_list)

        return self.word
        

    def create_spaces(self):
        spaces = []   
        for i in range(len(self.word)):
            spaces.append( '_')

        for i in range(len(spaces)):
            print(spaces[i], end = ' ')

        return spaces

           


# puzzle = Puzzle()

# puzzle.random_word()

# puzzle.spaces()



