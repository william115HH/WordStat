from wordstat import remove_punctuation, clean_words, average_word_length, remove_stopwords


def test_remove_punctuation():
    assert remove_punctuation("Hello, world!") == "Hello world"


def test_clean_words_lowercases():
    assert clean_words("The Cat") == ["the", "cat"]


def test_average_word_length():
    assert average_word_length(["ab", "abcd"]) == 3.0


def test_clean_words_empty():
    assert clean_words("") == []


def test_clean_words_punctuation_only():
    assert clean_words("!!! ... ???") == []


def test_average_word_length_empty():
    assert average_word_length([]) == 0.0


def test_remove_stopwords():
    assert remove_stopwords(["the", "cat", "sat", "on", "the", "mat"]) == ["cat", "sat", "mat"]


def test_remove_stopwords_empty():
    assert remove_stopwords([]) == []