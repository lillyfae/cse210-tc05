import random

class Puzzle:
    '''The purpose of this class is to randomly select a word from the word list.
    
    Sterotyope:
        Game display

    Attributes:
        word_list (list): a list of words for the puzzle to choose from
        chosen_word (string): a random word from the word list
        create_spaces (list of strings): a list of characters that will initially contain spaces and be filled in with player guesses
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

        self.chosen_word = self.random_word()
        self.create_spaces()
    
    def random_word(self):
        '''Gets a random word from the word list. 

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns: the word
        '''
        return random.choice(self.word_list)

    def create_spaces(self):
        '''Creates the list of spaces

        Args:
           self (Puzzle)
           '''
        self.spaces = []   
        for i in range(len(self.chosen_word)):
            self.spaces.append('_')

    def print_spaces(self):
        '''Prints out the spaces

        Args:
           self (Puzzle)
           '''
        for ch in self.spaces:
            print(ch + " ", end='')
        print('\n')

