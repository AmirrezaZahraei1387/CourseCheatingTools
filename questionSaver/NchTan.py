import questionSaver.choice as choice


class NChoiceTAnswer:

    __title: str = ""
    __choices: list = []
    __name: str
    names: list = []

    def __init__(self, title, choices: list, name):
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

        if name in self.names:
            raise IndexError("the name provided for the question is not unique")
        self.__name = name
        self.names.append(self.__name)

    @property
    def title(self):
        return self.__title

    def getChoice(self, index):
        return self.__choices[index]

    def setChoice(self, index):
        """this function will set the mode of a choice.
        true if it is true and false if the choice is incorrect"""
        self.__choices[index].mode = index

    @property
    def name(self):
        return self.__name

    def searchChoice(self, txt):

        index = -1

        for ch in self.__choices:
            index += 1
            if choice.txtEq(txt, ch.title):
                return index
        return -1

    def getAnswers(self):

        answers = {"TRUE": [], "FALSE": [], "NONE": []}
        # true are the indicis if the choices that are true.
        # false is the indicis of the choices that are wrong
        # none are the indicis that are not clear weather true or not

        index = -1

        for ch in self.__choices:
            index += 1
            if ch.mode is True:
                answers["TRUE"].append(index)

            elif ch.mode is False:
                answers["FALSE"].append(index)

            elif ch.mode is None:
                answers["NONE"].append(index)

        return answers

