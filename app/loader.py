from .answer import Answer, AnswerType
from .question import Question


class Loader:
    """Class responsible for loading data from files into memory.

    :param filename_test: The filename for the test data
    :type filename_test: str
    """

    def __init__(self, filename_test: str):
        """Constructor method"""
        self.filename_test = filename_test

    def read_test_file(self) -> list:
        """Read test questions from the test file.
        
        :return: List of downloaded test questions
        :rtype: list
        """
        test = []
        with open(self.filename_test, "r", encoding="utf-8") as f:
            for line in f:
                answers = []
                for i in range(3):
                    type_answ = self.determine_type_answer(i)
                    answer = Answer(type_answ, f.readline())
                    answers.append(answer)
                question = Question(line, answers)
                test.append(question)
        return test


    def determine_type_answer(self, i: int) -> AnswerType:
        """Determine the type of answer based on the index.

        :param i: The index used to determine the answer type
        :type i: int
        :return: The type of the answer
        :rtype: AnswerType
        """
        type_answ = None
        if i == 0:
            if len(self.test) < 5:
                type_answ = AnswerType.GREEN
            elif len(self.test) < 10:
                type_answ = AnswerType.BLUE
            else:
                type_answ = AnswerType.RED
        elif i == 1:
            if len(self.test) < 5:
                type_answ = AnswerType.BLUE
            elif len(self.test) < 10:
                type_answ = AnswerType.RED
            else:
                type_answ = AnswerType.GREEN
        elif i == 2:
            if len(self.test) < 5:
                type_answ = AnswerType.RED
            elif len(self.test) < 10:
                type_answ = AnswerType.GREEN
            else:
                type_answ = AnswerType.BLUE
        return type_answ

    def read_green_file(self, filename_green: str) -> str:
        """Read the contents of the file for green results.
        
        :param filename_green: The file name for the result of green responses
        :type filename_green: str
        :return: result for green responses
        :rtype: str
        """
        with open(filename_green, "r", encoding="utf-8") as f:
            green = f.read()
            return green

    def read_red_file(self, filename_red: str) -> str:
        """Read the contents of the file for red results.

        :param filename_red: The file name for the result of red responses
        :type filename_red: str
        :return: result for red responses
        :rtype: str
        """
        with open(filename_red, "r", encoding="utf-8") as f:
            red = f.read()
            return red

    def read_blue_file(self, filename_blue: str) -> str:
        """Read the contents of the file for blue results.

        :param filename_blue: The file name for the result of blue responses
        :type filename_blue: str
        :return: result for blue responses
        :rtype: str
        """
        with open(filename_blue, "r", encoding="utf-8") as f:
            blue = f.read()
            return blue


    