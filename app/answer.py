from enum import Enum, auto


class AnswerType(Enum):
    """An enumeration representing which type the response belongs to."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Answer:
    """Class representing an answer with its type and text.

    :param type_: The type of the answer
    :type type_: AnswerType
    :param text: The text of the answer
    :type text: str
    """

    def __init__(self, type_: AnswerType, text: str):
        """Constructor method"""
        self.type_ = type_
        self.text = text

    def __str__(self):
        """Return a string representation of the Answer instance.

        :return: representation of the Answer instance
        :rtype: str
        """
        return f"Answer: {self.text} {self.type_}"