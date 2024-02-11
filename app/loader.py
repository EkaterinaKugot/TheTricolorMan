from .answer import Answer, AnswerType
from .question import Question


class Loader:
    """Class responsible for loading data from files into memory.

    :param filename_test: The filename for the test data
    :type filename_test: str
    :param filename_green: The file name for the result of green responses
    :type filename_green: str
    :param filename_red: The file name for the result of red responses
    :type filename_red: str
    :param filename_blue: The file name for the result of blue responses
    :type filename_blue: str
    :param green: Content read from file for green result
    :type green: str
    :param blue: Content read from file for blue result
    :type blue: str
    :param red: Content read from file for red result
    :type red: str
    :param test: A list to store the loaded test questions
    :type test: list
    """

    def __init__(
        self,
        filename_test: str,
        filename_green: str,
        filename_red: str,
        filename_blue: str,
    ):
        """Constructor method"""
        self.filename_test = filename_test
        self.filename_green = filename_green
        self.filename_red = filename_red
        self.filename_blue = filename_blue
        self.green = None
        self.blue = None
        self.red = None
        self.test = []

    def read_test_file(self) -> None:
        """Read test questions from the test file."""
        with open(self.filename_test, "r", encoding="utf-8") as f:
            for line in f:
                answers = []
                for i in range(3):
                    type_answ = self.determine_type_answer(i)
                    answer = Answer(type_answ, f.readline())
                    answers.append(answer)
                question = Question(line, answers)
                self.test.append(question)

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

    def read_green_file(self) -> None:
        """Read the contents of the file for green results."""
        with open(self.filename_green, "r", encoding="utf-8") as f:
            self.green = f.read()

    def read_red_file(self) -> None:
        """Read the contents of the file for red results."""
        with open(self.filename_red, "r", encoding="utf-8") as f:
            self.red = f.read()

    def read_blue_file(self) -> None:
        """Read the contents of the file for blue results."""
        with open(self.filename_blue, "r", encoding="utf-8") as f:
            self.blue = f.read()


    