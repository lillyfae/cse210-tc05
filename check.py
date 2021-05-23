
class Check:

    '''The purpose of this class is to receive the players guess and check if it is correct

    Stereotype:
        Checks answers

    Attributes:
        incorrect_guesses (integer) = keeps track of the amount of times the player guesses wrong
        letter_guessed (string) = it is the letter the player guessed
    '''

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Check): an instance of Check.
        """
        self.incorrect_guesses = 0
        self.letter_guessed = " "


    def guess(self):
        '''asks for the the players guess
        
        Args:
            self (Check): an instance of Check.
        '''
        
        self.letter_guessed = input("Guess a letter [a-z]: ")


    def check(self, word, spaces):  
        '''checks if the guess is correct, if it is correct then it fills in an empty space with the letter. 
            It also updates and keeps track of the amount of incorrect guesses
            
        Args:
            self (Check): an instance of Check.
        '''
        found = False
        for i in range(0, len(word)):    
            if word[i] == self.letter_guessed:
                spaces[i] = self.letter_guessed    
                found = True
        if not found:
            self.incorrect_guesses += 1
        return spaces
