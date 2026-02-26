from src.preprocessing import TextPreprocessor


def test_strip_punctuation_removes_symbols():
    preprocessor = TextPreprocessor()
    assert preprocessor.strip_punctuation("hello!!!") == "hello"


def test_tokenize_lowercases_and_cleans_words():
    preprocessor = TextPreprocessor()
    result = preprocessor.tokenize("Hello, World!!!")
    assert result == ["hello", "world"]


def test_tokenize_removes_empty_tokens():
    preprocessor = TextPreprocessor()
    result = preprocessor.tokenize("... !!! test")
    assert result == ["test"]