import pytest
from Automation.paloalto_interview.paloalto_best_solution import count_word_occurrences

@pytest.mark.parametrize("text, word, expected", [
    ("Python is great. I love python! Do you like Python too?", "python", 3),
    ("Hello, hello! HELLO...", "hello", 3),
    ("This is a test of the testing system.", "test", 1),
    ("", "python", 0),
    ("Python python python", "", 0),
    (None, "python", 0),
    ("python", None, 0),
    ("A python is not pythonic.", "python", 1),
    ("Do you know PyThOn? python, PYTHON!", "python", 3)
])
def test_count_word_occurrences(text, word, expected):
    assert count_word_occurrences(text, word) == expected



# @pytest.mark.parametrize("text, word", [
#     (123, "python"),
#     ("python", 123),
#     (["a", "b"], "a"),
#     ("python", ["p", "y"]),
#     ({"text": "python"}, "python"),
#     ("python", {"w": "python"}),
# ])
# def test_count_word_occurrences_invalid_types(text, word):
#     with pytest.raises(TypeError):
#         count_word_occurrences(text, word)