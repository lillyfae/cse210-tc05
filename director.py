from puzzle import Puzzle
from jumper import Jumper
from check import Check


class Director:

    '''A code outline for the director of the jumper game. The purpose of this class is to '''

    def __init__(self):
        self.puzzle = Puzzle()
        self.jumper = Jumper()
        self.check = Check()
        self.word = [] 
        self.keep_playing = True
        self.guess = False
        self.incorrect_guesses = 0
        
    
    def start_game(self):
        self.word = self.puzzle.random_word()

        while self.keep_playing:
            self.display_game()
            self.guess_and_check()
        

    def display_game(self):
        '''This shows and displays the game borad and the paerchueter'''

        self.puzzle.spaces()
        self.jumper.jumper(self.incorrect_guesses)
        

    def guess_and_check(self):
        '''Takes the players guess and checks if it is correct. It updates and keeps track of the amount of incorrect guesses'''
        
        letter_guessed = input("Guess a letter [a-z]: ")

        for i in range(len(self.word)):
            if letter_guessed == self.word[i]:
                guess = True
            else:
                guess = False
                incorrect_guesses += 1

        


    
        

    