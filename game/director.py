from puzzle import Puzzle
from jumper import Jumper
from check import Check


class Director:

    '''A code outline for the director of the jumper game. The purpose of this class is to control the suquence of play 

    Stereotype:
        Controller

    Attributes:
        puzzle (Puzzle): An instance of the class of objects known as Puzzle.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        check (Check): An instance of the class of objects known as Check.
        keep_playing (boolean): Whether or not the game can continue.
    '''


    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.puzzle = Puzzle()
        self.jumper = Jumper()
        self.check = Check()
        self.keep_playing = True        
    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        
        keep_playing = True
        while keep_playing:
            self.puzzle.print_spaces()
            self.jumper.print_jumper(self.check.incorrect_guesses)
            self.guess_and_check()
            print("\n\n")
            keep_playing = self.is_game_still_going()
        

    def guess_and_check(self):
        '''This asks player for guess and updates game based on guess
        
        Args:
            self (Director): An instance of Director.
        '''
        self.check.guess()
        self.puzzle.spaces = self.check.check(self.puzzle.chosen_word, self.puzzle.spaces)
    
    def is_game_still_going(self):
        '''This checks if the player has won or lost
        
        Args:
            self (Director): An instance of Director.
        '''
        if self.check.incorrect_guesses == 4:
            self.jumper.dead_head()
            self.jumper.print_jumper(self.check.incorrect_guesses)
            print("You Lose")
            return False
        elif "_" not in self.puzzle.spaces:
            print("You Win!") 
            self.puzzle.print_spaces()
            return False
        else:
            return True
        
        
        


        


    
        

    