from puzzle import Puzzle
from check import Check
import pytest as py


def test_check():
    check = Check()
    check.letter_guessed = "a"
    word = "frog"
    spaces = ["_", "_", "_", "_"]
    check.check(word, spaces) 
    assert check.incorrect_guesses == 1

def test_create_spaces():
    puzzle = Puzzle()
    puzzle.chosen_word = "cat"
    puzzle.create_spaces()
    
    assert len(puzzle.spaces) == 3
    
    for space in puzzle.spaces:
        assert space == "_"
        assert space != "+"

def test_random_word():
    puzzle = Puzzle()
    random_word = "inch"
    found = False
    for word in puzzle.word_list:
        if random_word == word:
            found = True
            break

    assert found == True



#calls test functions when main is called
py.main(["-v", "--tb=no", "test_cse210-tc05.py"])

