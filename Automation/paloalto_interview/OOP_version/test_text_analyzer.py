import pytest
from Automation.paloalto_interview.OOP_version.text_anlyzer import TextAnalyzer


class TestTextAnalyzerPositiveCases:

    @pytest.mark.parametrize("text, word, expected", [
        ("Python is great. I love python! Do you like Python too?", "python", 3),
        ("Hello, hello! HELLO...", "hello", 3),
        ("This is a test of the testing system.", "test", 1),
        ("", "python", 0),
        ("Python python python", "", 0),
        (None, "python", 0),
        ("A python is not pythonic.", "python", 1),
        ("Do you know PyThOn? python, PYTHON!", "python", 3),
    ])
    def test_word_count_valid(self, text, word, expected):
        analyzer = TextAnalyzer(text)
        assert analyzer.count_word_occurrences(word) == expected


class TestTextAnalyzerNegativeCases:

    @pytest.mark.parametrize("text, word", [
        (123, "python"),
        ("python", 123),
        (["a", "b"], "a"),
        ("python", ["p", "y"]),
        ({"text": "python"}, "python"),
        ("python", {"w": "python"}),
    ])
    def test_invalid_input_types(self, text, word):
        if not isinstance(text, str) and text is not None:
            with pytest.raises(TypeError):
                TextAnalyzer(text)
        else:
            analyzer = TextAnalyzer(text)
            with pytest.raises(TypeError):
                analyzer.count_word_occurrences(word)
