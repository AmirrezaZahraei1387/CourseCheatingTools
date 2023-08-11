"""a choice is one of the possible answers to a questions.
it could be true or false."""
from difflib import SequenceMatcher


class Choice:

    __title: str
    __mode: bool = None

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

    def __str__(self):
        return self.__title


ACCEPTED_RANGE = 0.85


def txtEq(txt1: str, txt2: str):
    """this will get a text and the list of the choices.
    then it will say if one of the choices is approximately equal to
    the given text or not. it will check it approximately because
    the user may enter the txt a little different."""

    res = SequenceMatcher(None, txt1, txt2).ratio()
    return res >= ACCEPTED_RANGE

