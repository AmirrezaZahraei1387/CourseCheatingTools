import questionSaver.choice as choice



class NChoiceTAnswer:

    __title: str = ""
    __choices: list = []

    def __init__(self, title, choices):
        """title is the title of the question and the choices are the choices.
        for example in the following example:

        what is an apple?
        1 - animal
        2 - human
        3 - food
        4 - fruit

        what is an apple is title and the rest is choices."""

        self.__title = title
        self.__choices = choices

    @property
    def title(self):
        return self.__title

    def getChoice(self, index):
        return self.__choices[index]

    def setChoice(self, index):
        """this function will set the mode of a choice.
        true if it is true and false if the choice is incorrect"""
        self.__choices[index].mode = index

    def searchChoice(self, txt):

        index = -1

        for ch in self.__choices:
            index += 1
            if choice.txtEq(txt, ch.title):
                return index
        return -1





