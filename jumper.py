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

    def jumper(self):
        print(self.string_1)
        print(self.string_2)
        print(self.string_3)
        print(self.string_4)
        print(self.head)
        print(self.body)
        print(self.legs)

jumper = Jumper()

jumper.jumper()