
class Check:

    def __init__(self):
        self.incorrect_guesses = 0
        self.letter_guessed = " "


    def guess(self):
        '''asks for the the players guess'''
        
        self.letter_guessed = input("Guess a letter [a-z]: ")


    def check(self, word, spaces):  
        '''checks if the guess is correct, if it is correct then it fills in an empty space with the letter. It also updates and keeps track of the amount of incorrect guesses'''
        found = False
        for i in range(0, len(word)):    
            if word[i] == self.letter_guessed:
                spaces[i] = self.letter_guessed    
                found = True
        if not found:
            self.incorrect_guesses += 1
        return spaces
