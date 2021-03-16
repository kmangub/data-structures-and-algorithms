import pytest
from challenges.repeated_word.repeated_word import repeated_word

def test_one_repeated_word():
    string = "Have a wonderful day. The day was not wonderful."
    assert repeated_word(string) == 'day'
def test_two_repeated_word_no_matches():
    string = "Have a wonderful day. The morning was fun."
    assert repeated_word(string) == 'No matches'
def test_three_repeated_word_no_matches():
    string = "Have a wonderful day. The morning was Wonderful."
    assert repeated_word(string) == 'wonderful'