from puzzle import Puzzle
from jumper import Jumper
from check import Check


class Director:

    '''A code outline for the director of the jumper game. The purpose of this class is to '''

    def __init__(self):
        self.puzzle = Puzzle()
        self.jumper = Jumper()
        self.check = Check()
        self.keep_playing = True
        self.spaces = []
        self.word = " "
        
    
    def start_game(self):
        '''This displays the puzzle, starts the game and continues until there is a win or a loss'''
        self.puzzle.create_spaces()
        self.jumper.jumper(self.check.incorrect_guesses)
        self.word = self.puzzle.random_word()
        

        while self.keep_playing:
            self.guess_and_check()
            self.display_game()
            self.is_game_still_going()
        

    def guess_and_check(self):
        '''This asks player for guess and updates game based on guess'''
        self.check.guess()
        self.check.check(self.word, self.puzzle.create_spaces())
        

    def display_game(self):
        '''This shows and displays the new game borad and the paerchueter'''

        for i in range(len(self.check.spaces)):
            print(self.check.spaces[i], end = ' ')
        
        self.jumper.jumper(self.check.incorrect_guesses)

    
    
    def is_game_still_going(self):
        '''This checks if the player has won or lost'''
       
        if self.check.incorrect_guesses == 4:
            self.jumper.jumper(self.check.incorrect_guesses)
            self.keep_playing = False
            print("You Lose")

        elif "_" not in self.check.spaces:
            self.keep_playing = False
            print("You Win")
        
        else:
            self.keep_playing = True 
        
        
        


        


    
        

    