from src.lexicon_loader import load_word_set


def test_load_word_set_reads_words_and_skips_comments(tmp_path):
    file_path = tmp_path / "words.txt"
    file_path.write_text(";comment line\nhappy\nsad\n\n", encoding="utf-8")

    result = load_word_set(str(file_path))

    assert result == {"happy", "sad"}