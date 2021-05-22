
class Check:

    def __init__(self):
        self.incorrect_guesses = 0
        self.letter_guessed = " "
        self.word_array = [] 
        self.spaces = []


    def guess(self):
        '''asks for the the players guess'''
        
        self.letter_guessed = input("Guess a letter [a-z]: ")


    def check(self, word, spaces):  
        '''checks if the guess is correct, if it is correct then it fills in an empty space with the letter. It also updates and keeps track of the amount of incorrect guesses'''
        self.spaces = spaces
        self.word_array = list(word)

        for i in range(len(self.word_array)):
    
            if self.letter_guessed in self.word_array[i]:
                self.spaces[i] = self.letter_guessed
            
            elif self.letter_guessed not in self.word_array:
                self.incorrect_guesses += 1
                break
        
            

        
            
