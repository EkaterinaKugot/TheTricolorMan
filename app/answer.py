from enum import Enum, auto

class AnswerType(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

class Answer:
    def __init__(self, type_: AnswerType, text: str):
        self.type_ = type_
        self.text = text

    def __str__(self):
        return f"Answer: {self.text}, {self.type_}"