from .answer import Answer, AnswerType
from .question import Question
import os


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
        
        :raises FileNotFoundError: The path to the test file was not found
        :return: List of downloaded test questions
        :rtype: list
        """
        test = []
        test_file = Loader.current_path(self.filename_test)
        if(os.path.isfile(test_file)):
            with open(test_file, "r", encoding="utf-8") as f:
                for line in f:
                    answers = []
                    for i in range(3):
                        type_answ = self.determine_type_answer(i, test)
                        answer = Answer(type_answ, f.readline().rstrip())
                        answers.append(answer)
                    question = Question(line.rstrip(), answers)
                    test.append(question)
        else:
            raise FileNotFoundError("The test file does not exist")
        return test
    
    @staticmethod
    def current_path(filename: str) -> str:
        """Creates the correct path to text files in the data folder
        
        :param filename: Text file name
        :type filename: str
        :return: Returns the full and correct path to the file
        :rtype: str
        """
        currentdir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(currentdir, "data", filename)
        return path

    def determine_type_answer(self, i: int, test: list) -> AnswerType:
        """Determine the type of answer based on the index.

        :param i: The index used to determine the answer type
        :type i: int
        :param test: List of downloaded test questions
        :type test: list
        :return: The type of the answer
        :rtype: AnswerType
        """
        type_answ = None
        if i == 0:
            if len(test) < 5:
                type_answ = AnswerType.GREEN
            elif len(test) < 10:
                type_answ = AnswerType.BLUE
            else:
                type_answ = AnswerType.RED
        elif i == 1:
            if len(test) < 5:
                type_answ = AnswerType.BLUE
            elif len(test) < 10:
                type_answ = AnswerType.RED
            else:
                type_answ = AnswerType.GREEN
        elif i == 2:
            if len(test) < 5:
                type_answ = AnswerType.RED
            elif len(test) < 10:
                type_answ = AnswerType.GREEN
            else:
                type_answ = AnswerType.BLUE
        return type_answ

    def read_green_file(self, filename_green: str) -> str:
        """Read the contents of the file for green results.
        
        :param filename_green: The file name for the result of green responses
        :type filename_green: str
        :raises FileNotFoundError: Green results file path not found
        :return: Result for green responses
        :rtype: str
        """
        filename = self.current_path(filename_green)
        if(os.path.isfile(filename)):
            with open(filename, "r", encoding="utf-8") as f:
                green = f.read()
                return green
        raise FileNotFoundError("The green file does not exist")
        
    def read_red_file(self, filename_red: str) -> str:
        """Read the contents of the file for red results.

        :param filename_red: The file name for the result of red responses
        :type filename_red: str
        :raises FileNotFoundError: Red results file path not found
        :return: Result for red responses
        :rtype: str
        """
        filename = self.current_path(filename_red)
        if(os.path.isfile(filename)):
            with open(filename, "r", encoding="utf-8") as f:
                red = f.read()
                return red
        raise FileNotFoundError("The red file does not exist")

    def read_blue_file(self, filename_blue: str) -> str:
        """Read the contents of the file for blue results.

        :param filename_blue: The file name for the result of blue responses
        :type filename_blue: str
        :raises FileNotFoundError: BLue results file path not found
        :return: Result for blue responses
        :rtype: str
        """
        filename = self.current_path(filename_blue)
        if(os.path.isfile(filename)):
            with open(filename, "r", encoding="utf-8") as f:
                blue = f.read()
                return blue
        raise FileNotFoundError("The blue file does not exist")