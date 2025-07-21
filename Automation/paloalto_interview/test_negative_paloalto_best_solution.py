import pytest
from Automation.paloalto_interview.paloalto_best_solution import count_word_occurrences

@pytest.mark.parametrize("text, word", [
    (123, "python"),
    ("python", 123),
    (["a", "b"], "a"),
    ("python", ["p", "y"]),
    ({"text": "python"}, "python"),
    ("python", {"w": "python"}),
])
def test_count_word_occurrences_invalid_types(text, word):
    with pytest.raises(TypeError):
        count_word_occurrences(text, word)
