def load_word_set(file_path: str) -> set[str]:
    """
    Function: load_word_set
    Purpose: Load sentiment words from a text file into a set.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Input:
    - file_path: path to the text file containing sentiment words

    Output:
    - A set of words, excluding blank lines and comment lines
    """

    words = set()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            word = line.strip()

            # Ignore empty lines and comment lines
            if word and not word.startswith(";"):
                words.add(word)

    return words