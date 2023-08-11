import questionSaver as qs
import sys


def get_mode_choice():
    while True:
        mode = input("enter the state of the question?(N/ T/ F): ")

        if mode == "N":
            return None

        elif mode == "T":
            return True

        elif mode == "F":
            return False
        else:
            print("the mode entered is incorrect")


def get_question():
    title = input("enter the question title: ")
    choices = []

    while True:

        choice = input("enter choice: ")
        mode = get_mode_choice()
        isContinue = input("enter 0 to finish or any thing else to continue: ")

        c = qs.Choice(choice)
        c.mode = mode
        choices.append(c)

        if isContinue == "0":
            break

    while True:

        name = input("enter a unique name for the question: ")

        if name in qs.NChoiceTAnswer.names:
            print("the name is not unique.")
        else:
            break

    return qs.NChoiceTAnswer(title, choices, name)


allQuestions = qs.MultipleQuestionS([])

while True:

    command = input("enter what you want to do?").lower()

    if command == "add-question":
        allQuestions.append(get_question())

    if command == "show-all-questions":
        pass

    elif command == "set-choice-mode":
        pass

    elif command == "add-choice":
        pass

    elif command == "remove-question":
        pass

    elif command == "get-answer":
        pass

    elif command == "exit":
        break

    else:
        print("the given command is not recognized")
