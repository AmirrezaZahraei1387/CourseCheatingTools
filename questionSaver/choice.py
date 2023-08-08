"""a choice is one of the possible answers to a questions.
it could be true or false."""
from nltk.tokenize import word_tokenize


class Choice:

    __title: str
    __mode: bool

    def __init__(self, title: str):
        self.__title = title

    @property
    def title(self):
        return self.__title

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, m: bool):
        """m is the mode for the choice. it defines
        if the choice is true or false."""
        self.__mode = m


ACCEPTED_RANGE = 3


def choiceEq(txt: str, choice: Choice):
    """this will get a text and the list of the choices.
    then it will say if one of the choices is approximately equal to
    the given text or not. it will check it approximately because
    the user may enter the txt a little different."""

    words_txt = word_tokenize(txt)
    words_choice = word_tokenize(choice.title)
    length_word_choice = len(words_choice)

    found_words = 0

    for word in words_txt:
        if word in words_choice:
            found_words += 1

    if found_words > length_word_choice - ACCEPTED_RANGE:
        return True
    return False
