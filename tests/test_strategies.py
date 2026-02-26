from src.preprocessing import TextPreprocessor
from src.strategies import LexiconSentimentStrategy


def test_score_counts_positive_words():
    preprocessor = TextPreprocessor()
    strategy = LexiconSentimentStrategy(
        positive_words={"good", "happy"},
        negative_words={"bad", "sad"},
        preprocessor=preprocessor
    )

    pos, neg, net = strategy.score("Good and happy day")
    assert pos == 2
    assert neg == 0
    assert net == 2


def test_score_counts_negative_words():
    preprocessor = TextPreprocessor()
    strategy = LexiconSentimentStrategy(
        positive_words={"good", "happy"},
        negative_words={"bad", "sad"},
        preprocessor=preprocessor
    )

    pos, neg, net = strategy.score("Bad and sad day")
    assert pos == 0
    assert neg == 2
    assert net == -2


def test_score_handles_mixed_sentiment():
    preprocessor = TextPreprocessor()
    strategy = LexiconSentimentStrategy(
        positive_words={"good"},
        negative_words={"bad"},
        preprocessor=preprocessor
    )

    pos, neg, net = strategy.score("good bad good")
    assert pos == 2
    assert neg == 1
    assert net == 1