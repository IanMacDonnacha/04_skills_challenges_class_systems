# File: tests/test_vowel_remover.py

"""
A colleague has done a code review and has advised that the tests should cover all the vowels.

Add a new unit test to check that the program can remove all the vowels from "aeiou", returning an empty string, "".

"""
from lib.vowel_remover import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."

def test_to_remove_all_vowels_from_a_string():
    remover = VowelRemover("aeiou")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == ""

