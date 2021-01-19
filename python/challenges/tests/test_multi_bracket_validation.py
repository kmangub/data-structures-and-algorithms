import pytest
from challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation_with_one_pair():
    actual = multi_bracket_validation('{}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_one__of_each_pair():
    actual = multi_bracket_validation('{}(){}')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_extra_characters():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_pair_inside_of_pair():
    actual = multi_bracket_validation('(){}[[]]')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_words_separated():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    expected = True
    assert actual == expected

def test_multi_bracket_validation_with_missing_closing():
    actual = multi_bracket_validation('[({}]')
    expected = False
    assert actual == expected

def test_multi_bracket_validation_with_no_corresponding_opening():
    actual = multi_bracket_validation('(](')
    expected = False
    assert actual == expected

def test_multi_bracket_validation_with_no_matching_pairs():
    actual = multi_bracket_validation('{(})')
    expected = False
    assert actual == expected

