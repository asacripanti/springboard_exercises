"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, path):
           """
        Initialize the WordFinder with a path to a file containing words.

        """
           self.words = self.parse_file(path)
           print(f"{len(self.words)} words read")

    def parse_file(self, path):
        """Return a list of words."""
        with open(path, "r") as file:
            return [word.strip() for word in file]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)
    


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments."""

    def parse_file(self, path):
        """Return a list of words, skipping blanks and comments."""
        with open(path, "r") as file:
            return [word.strip() for word in file if word.strip() and not word.startswith("#")]



# Example usage
path = "/Users/alejandrosacripanti/Desktop/springboard/exercises/python-oo-practice/words.txt"
wf = WordFinder(path)

random_word = wf.random()
print(random_word)

    
