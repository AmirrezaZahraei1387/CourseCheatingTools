

class MultipleQuestionS:
    __questions: list = []

    def __init__(self, questions: list):
        self.__questions = questions

    def __getitem__(self, index):
        return self.__questions[index]

    def __setitem__(self, key, value):
        self.__questions[key] = value

    def append(self, value):
        self.__questions.append(value)
