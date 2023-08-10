from questionSaver.choice import txtEq


class MultipleQuestionS:
    __questions: list = []
    __name: str

    def __init__(self, questions: list):
        self.__questions = questions

    def __getitem__(self, index):
        return self.__questions[index]

    def __setitem__(self, key, value):
        self.__questions[key] = value

    def append(self, value):
        self.__questions.append(value)

    def searchQuestion(self, value: str, mode: str):
        """value is something you which to search, and mode is the
        mode for searching it could be EXACT or SIMILAR.
        EXACT means to do this using operator ==.
        and SIMILAR means to search using text similarities."""
        index = -1

        if mode.lower() == "exact":
            for q in self.__questions:
                index += 1
                if q == value:
                    return index
            return -1

        elif mode.lower() == "similar":
            results = []
            for q in self.__questions:
                index += 1
                if txtEq(value, q.name):
                    results.append(index)
            return results

        else:
            raise ValueError("unrecognized mode.")



