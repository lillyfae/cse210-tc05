from game.puzzle import Puzzle
from game.jumper import Jumper
from game.check import Check


class Director:

    '''A code outline for the director of the jumper game. The purpose of this class is to '''

    def __init__(self):
        self.puzzle = Puzzle()
        self.jumper = Jumper()
        self.check = Check()
        self.keep_playing = True
        self.spaces = []
        
    
    def start_game(self):
        '''This displays the puzzle, starts the game and continues until there is a win or a loss'''
        self.spaces = puzzle.create_spaces()
        self.jumper.jumper(self.check.incorrect_guesses)

        while self.keep_playing:
            self.guess_and_check()
            self.display_game()
            self.is_game_still_going()
        

    def guess_and_check(self):
        '''This asks player for guess and updates game based on guess'''
        self.check.guess()
        self.spaces = self.check.check(self.puzzle.random_word())
        

    def display_game(self):
        '''This shows and displays the new game borad and the paerchueter'''

        for i in range(len(spaces)):
            print(spaces[i], end = ' ')
        
        self.jumper.jumper(self.check.incorrect_guesses)

    
    
    def is_game_still_going(self):
        '''This checks if the player has won or lost'''
       
        if incorrect_guesses == 4:
            self.jumper.jumper(self.check.incorrect_guesses)
            self.keep_playing = False
            print("You Lose")

        elif "_" not in spaces:
            self.keep_playing = False
            print("You Win")
        
        else:
            self.keep_playing = True
        
        
        


        


    
        

    