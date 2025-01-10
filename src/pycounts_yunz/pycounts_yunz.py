# The code below is cited from "py-pkgs.org/03-how-to-package-a-python".
# The code below is only used to practice how to make a package in Python.
# The link of the original code is (Section 3.4.): 
# https://py-pkgs.org/03-how-to-package-a-python#counting-words-in-a-text-file

from collections import Counter
from string import punctuation


def load_text(input_file):
    """Load text from a text file and return as a string."""
    with open(input_file, "r") as file:
        text = file.read()
    return text
    
def clean_text(text):
    """Lowercase and remove punctuation from a string."""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text
    
def count_words(input_file):
    """Count unique words in a string."""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)