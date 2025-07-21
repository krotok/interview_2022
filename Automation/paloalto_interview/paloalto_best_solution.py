from typing import Optional
import string

def count_word_occurrences(text: str, word: str) -> int:
    """
    Подсчитывает количество вхождений слова в тексте без учёта регистра.
    Слова считаются отдельными, если они отделены пробелами или знаками препинания.

    :param text: Исходный текст
    :param word: Слово для поиска
    :return: Количество вхождений слова
    """

    if not text or not word:
        return 0

    if not isinstance(text, str) or not isinstance(word, str):
        raise TypeError("Both 'text' and 'word' must be strings")

    # Приводим к нижнему регистру
    text = text.lower()
    word = word.lower()

    # Удаляем знаки препинания
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    # Разбиваем текст на слова
    words = cleaned_text.split()

    # Считаем точные совпадения
    return sum(1 for w in words if w == word)