# The code below is cited from "py-pkgs.org/03-how-to-package-a-python".
# The code below is only used to practice how to make a package in Python.
# The link of the original code is (Section 3.5.): 
# https://py-pkgs.org/03-how-to-package-a-python#counting-words-in-a-text-file

import matplotlib.pyplot as plt

def plot_words(word_counts, n=10):
    """Plot a bar chart of word counts."""
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    return fig