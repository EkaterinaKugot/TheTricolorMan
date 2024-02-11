from .answer import Answer


class Question:
    """Class representing a question with its text and answers.

    :param text: The text of the question
    :type text: str
    :param answers: A tuple containing response instances
    :type answers: tuple[Answer, ...]
    """

    def __init__(self, text: str, answers: tuple[Answer, ...]):
        """Constructor method"""
        self.text = text
        self.answers = answers

    def __str__(self):
        """Return a string representation of the Question instance.

        :return: representation of the Question instance
        :rtype: str
        """
        return f"Question: {self.text}\n{self.answers[0]}\n{self.answers[1]}\n{self.answers[2]}"