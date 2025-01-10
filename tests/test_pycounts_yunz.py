# The code below is cited from "py-pkgs.org/03-how-to-package-a-python".
# The code below is only used to practice how to make a package in Python.
# The link of the original code is (Section 3.7.2): 
# https://py-pkgs.org/03-how-to-package-a-python#counting-words-in-a-text-file

from pycounts_yunz.pycounts_yunz import count_words
from collections import Counter

def test_count_words():
    """Test word counting from a file."""
    expected = Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                        'the': 1, 'same': 1, 'thing': 1, 
                        'over': 2, 'and': 2, 'expecting': 1,
                        'different': 1, 'results': 1})
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"
