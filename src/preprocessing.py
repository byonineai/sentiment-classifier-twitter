import string


class TextPreprocessor:
    """
    Class: TextPreprocessor
    Purpose: Clean and tokenize tweet text before sentiment scoring.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Output:
    - Removes punctuation from words
    - Converts text into a list of cleaned lowercase tokens
    """

    def __init__(self, punctuation_chars=None):
        """
        Method: __init__
        Purpose: Initialize the list of punctuation characters to remove.

        Input:
        - punctuation_chars: optional custom list of punctuation characters

        Output:
        - Stores the punctuation characters used by the preprocessor
        """
        self.punctuation_chars = punctuation_chars or list(string.punctuation)

    def strip_punctuation(self, word: str) -> str:
        """
        Method: strip_punctuation
        Purpose: Remove punctuation characters from a single word.

        Input:
        - word: a string that may contain punctuation

        Output:
        - The cleaned word with punctuation removed
        """
        for p in self.punctuation_chars:
            word = word.replace(p, "")
        return word

    def tokenize(self, text: str) -> list[str]:
        """
        Method: tokenize
        Purpose: Convert text into cleaned lowercase tokens.

        Input:
        - text: a string of tweet text

        Output:
        - A list of cleaned words with punctuation removed
        """
        tokens = []

        for word in text.lower().split():
            clean_word = self.strip_punctuation(word)
            if clean_word:
                tokens.append(clean_word)

        return tokens