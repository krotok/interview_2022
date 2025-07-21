import string
from typing import Optional


class TextAnalyzer:
    """
    Класс для анализа текста.
    """

    def __init__(self, text: Optional[str]):
        if text is not None and not isinstance(text, str):
            raise TypeError("Text must be a string or None")
        self.text = text or ""

    def count_word_occurrences(self, word: str) -> int:
        """
        Подсчитывает количество вхождений слова в тексте без учёта регистра.
        Слова считаются отдельными, если они отделены пробелами или знаками препинания.

        :param word: Слово для поиска
        :return: Количество вхождений слова
        """
        if not isinstance(word, str):
            raise TypeError("Word must be a string")

        if not word:
            return 0

        cleaned_text = self._clean_text(self.text)
        words = cleaned_text.split()
        target = word.lower()

        return sum(1 for w in words if w == target)

    @staticmethod
    def _clean_text(text: str) -> str:
        """
        Приводит текст к нижнему регистру и удаляет знаки препинания.
        """
        translator = str.maketrans('', '', string.punctuation)
        return text.lower().translate(translator)
