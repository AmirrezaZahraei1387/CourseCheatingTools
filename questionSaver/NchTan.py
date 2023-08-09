import questionSaver.choice as choice



class NChoiceTAnswer:

    __title: str = ""
    __choices: list = []

    def __init__(self, title="", choices=None):
        """title is the title of the question and the choices are the choices.
        for example in the following example:

        what is an apple?
        1 - animal
        2 - human
        3 - food
        4 - fruit

        what is an apple is title and the rest is choices."""

        self.__title = title

        if choices is not None:
            self.__choices = choices



