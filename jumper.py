class Jumper:
    ''' This class is to layout the parachuter.
    
    Sterotype: 
        Game display

    Args:
        strings (list) = holds the layout of the parachute
        set_strings (method) = creates the list of strings for the parachute display
        head_index (integer) = Holds the new head of parachuter for when the player has lost
    '''
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.strings = []
        self.set_strings()
        self.head_index = 4
        

    def set_strings(self):
        """Creates a list of strings that hold the parachute display
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.strings.append(" _____")
        self.strings.append("/_____\\ ")
        self.strings.append("\     /")
        self.strings.append(" \   /")
        self.strings.append("   o")
        self.strings.append("  /|\\")
        self.strings.append("  / \\")

    def dead_head(self):
        """Replaces the circle head with new x head when player has lost
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self.strings[self.head_index] = "   x"

    def print_jumper(self, incorrect_guesses):
        """Displays the parachute
        
        Args:
            self (Jumper): an instance of Jumper.
            incorrect_guesses(integer): the amount of incorrect guesses
        """
         
        for i in range(incorrect_guesses, len(self.strings)):
             print(self.strings[i])