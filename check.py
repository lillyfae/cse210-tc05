
class check:

    def __init__(self):
        self.incorrect_guesses = 0
        self.letter_guessed = " "
        self.word_array = [] 


    def guess(self):
        '''asks for the the players guess'''
        
        self.letter_guessed = input("Guess a letter [a-z]: ")


    def check(self, word, spaces):  
        '''checks if the guess is correct, if it is correct then it fills in an empty space with the letter. It also updates and keeps track of the amount of incorrect guesses'''
        
        self.word_array = list(word)
        
        for i in range(word_array):
            if self.letter_guessed == self.word_array[i]:
                spaces[i] = self.word_array[i]
            
            else:
                incorrect_guesses += 1
        
        return spaces

            
