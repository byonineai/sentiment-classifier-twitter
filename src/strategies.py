from abc import ABC, abstractmethod
from .preprocessing import TextPreprocessor


class SentimentStrategy(ABC):
    """
    Class: SentimentStrategy
    Purpose: Define a common contract for any sentiment scoring method.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Output:
    - Ensures that all sentiment strategy classes implement a score method
    """

    @abstractmethod
    def score(self, text: str) -> tuple[int, int, int]:
        """
        Method: score
        Purpose: Compute sentiment scores from a text string.

        Input:
        - text: a string of tweet text

        Output:
        - A tuple containing:
          * positive_score
          * negative_score
          * net_score
        """
        pass


class LexiconSentimentStrategy(SentimentStrategy):
    """
    Class: LexiconSentimentStrategy
    Purpose: Compute sentiment scores using positive and negative word sets.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Dependencies:
    - positive_words
    - negative_words
    - TextPreprocessor

    Output:
    - Returns positive, negative, and net sentiment scores for a tweet
    """

    def __init__(
        self,
        positive_words: set[str],
        negative_words: set[str],
        preprocessor: TextPreprocessor
    ):
        """
        Method: __init__
        Purpose: Initialize the lexicon-based sentiment strategy.

        Input:
        - positive_words: set of positive sentiment words
        - negative_words: set of negative sentiment words
        - preprocessor: text preprocessing object

        Output:
        - Stores the word sets and preprocessor for sentiment analysis
        """
        self.positive_words = positive_words
        self.negative_words = negative_words
        self.preprocessor = preprocessor

    def score(self, text: str) -> tuple[int, int, int]:
        """
        Method: score
        Purpose: Count positive and negative words in a text and compute net score.

        Input:
        - text: a string of tweet text

        Output:
        - A tuple containing:
          * positive_score
          * negative_score
          * net_score
        """
        positive_word_count = 0
        negative_word_count = 0

        for word in self.preprocessor.tokenize(text):
            if word in self.positive_words:
                positive_word_count += 1
            if word in self.negative_words:
                negative_word_count += 1

        net_score = positive_word_count - negative_word_count
        return positive_word_count, negative_word_count, net_score