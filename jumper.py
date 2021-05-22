
class Jumper:
    ''' This class is to layout the parachuter.
    
    Sterotype: 
        Information holder

    Args:
        parachute strings
    '''
    def __init__(self):
        self.string_1 = " _____"
        self.string_2 = "/_____\\ "
        self.string_3 = "\     /"
        self.string_4 = " \   /"
        self.head = "   o"
        self.body = "  /|\\"
        self.legs = "  / \\"
        self.game_over_head = "   x"

    def jumper(self, incorrect_guesses):

        if incorrect_guesses == 0:
            print("")
            print("")
            print(self.string_1)
            print(self.string_2)
            print(self.string_3)
            print(self.string_4)
            print(self.head)
            print(self.body)
            print(self.legs)
        
        elif incorrect_guesses == 1:
            print("")
            print("")
            print(self.string_2)
            print(self.string_3)
            print(self.string_4)
            print(self.head)
            print(self.body)
            print(self.legs)

        elif incorrect_guesses == 2:
            print("")
            print("")
            print(self.string_3)
            print(self.string_4)
            print(self.head)
            print(self.body)
            print(self.legs)

        elif incorrect_guesses == 3:
            print("")
            print("")
            print(self.string_4)
            print(self.head)
            print(self.body)
            print(self.legs)
        
        # elif incorrect_guesses == 4:
        else:
            print("")
            print("")
            print(self.game_over_head)
            print(self.body)
            print(self.legs) 
        
    

# jumper = Jumper()

# jumper.jumper()