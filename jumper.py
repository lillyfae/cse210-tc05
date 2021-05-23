class Jumper:
    ''' This class is to layout the parachuter.
    
    Sterotype: 
        Information holder

    Args:
        parachute strings
    '''
    def __init__(self):
        self.strings = []
        self.set_strings()
        self.head_index = 4
        

    def set_strings(self):
        self.strings.append(" _____")
        self.strings.append("/_____\\ ")
        self.strings.append("\     /")
        self.strings.append(" \   /")
        self.strings.append("   o")
        self.strings.append("  /|\\")
        self.strings.append("  / \\")

    def dead_head(self):
        self.strings[self.head_index] = "   x"

    def print_jumper(self, incorrect_guesses):
         for i in range(incorrect_guesses, len(self.strings)):
             print(self.strings[i])