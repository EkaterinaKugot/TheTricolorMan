from .answer import AnswerType
from .loader import Loader
import random
import PySimpleGUI as sg
import matplotlib.pyplot as plt


class Test:
    """The class representing the test.

    :param loader: Instance of the Loader class
    :type loader: Loader
    :param rnd_questions: A list of randomly selected questions
    :type rnd_questions: list
    :param green: Number of green responses
    :type green: int
    :param red: Number of red responses
    :type red: int
    :param blue: Number of blue responses
    :type blue: int
    """

    def __init__(self, filename_test: str):
        """Constructor method"""
        self.loader = Loader(filename_test)
        self.rnd_questions = None
        self.green = 0
        self.red = 0
        self.blue = 0

    def random_questions(self) -> None:
        """Randomly shuffles questions and answers"""
        questions = self.loader.read_test_file()
        for q in questions:
            random.shuffle(q.answers)
        random.shuffle(questions)
        self.rnd_questions = questions

    def start(self) -> None:
        """Starts test with results"""
        self.random_questions()
        count = 0

        sg.theme("Reddit")
        question = sg.Text(
            self.rnd_questions[count].text,
            key="-QUE-",
            font=("Arial", 13),
            pad=((20, 0), (80, 0)),
        )
        answer1 = sg.Radio(
            "",
            "RADIO1",
            default=False,
            key="-ANSW1-",
            font=("Arial", 11),
            pad=((20, 0), (10, 0)),
        )
        text1 = sg.Text(
            self.rnd_questions[count].answers[0].text,
            key="-ANSW11-",
            font=("Arial", 11),
        )
        answer2 = sg.Radio(
            "",
            "RADIO1",
            default=False,
            key="-ANSW2-",
            font=("Arial", 11),
            pad=((20, 0), (10, 0)),
        )
        text2 = sg.Text(
            self.rnd_questions[count].answers[1].text,
            key="-ANSW22-",
            font=("Arial", 11),
        )
        answer3 = sg.Radio(
            "",
            "RADIO1",
            default=False,
            key="-ANSW3-",
            font=("Arial", 11),
            pad=((20, 0), (10, 0)),
        )
        text3 = sg.Text(
            self.rnd_questions[count].answers[2].text,
            key="-ANSW33-",
            font=("Arial", 11),
        )
        button = sg.Button(
            "Ответить",
            enable_events=True,
            key="-ANSWER-",
            font=("Arial", 16),
            pad=((355, 0), (30, 0)),
        )

        layout = [
            [question],
            [answer1, text1],
            [answer2, text2],
            [answer3, text3],
            [button],
        ]

        window = sg.Window('Test "The Tricolor Man"', layout, size=(850, 400))
        test_is_passed = False
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            elif event == "-ANSWER-":
                print(values)
                if not Test.checking_answer_selected(values):
                    continue
                count += 1
                if count == 15:
                    self.determining_answer(values, count)
                    test_is_passed = True
                    break
                else:
                    self.update(window, values, count)
        window.close()
        if test_is_passed:
            self.graphical_result()
            self.text_result()

    @staticmethod
    def checking_answer_selected(values: dict) -> bool:
        """Check if an answer is selected.

        :param values: A dictionary containing answers and their states
        :type values: dict
        :returns: True if an answer is selected, False otherwise
        :rtype: bool
        """
        is_true = False
        for _, val in values.items():
            if val == True:
                is_true = True
                break
        return is_true

    def update(self, window, values: dict, count: int) -> None:
        """Update the window with the next question.

        :param window: The PySimpleGUI window object
        :type window: class Window
        :param values: A dictionary containing answers and their states
        :type values: dict
        :param count: The current question number
        :type count: int
        """
        self.determining_answer(values, count)
        window["-QUE-"].update(self.rnd_questions[count].text)
        window["-ANSW11-"].update(self.rnd_questions[count].answers[0].text)
        window["-ANSW22-"].update(self.rnd_questions[count].answers[1].text)
        window["-ANSW33-"].update(self.rnd_questions[count].answers[2].text)
        window["-ANSW1-"].update(False)
        window["-ANSW2-"].update(False)
        window["-ANSW3-"].update(False)

    def determining_answer(self, values: dict, count: int):
        """Determine the answer and update scores.

        :param values: A dictionary containing answers and their states
        :type values: dict
        :param count: The current question number
        :type count: int
        """
        for key, value in values.items():
            if value == True:
                if key == "-ANSW1-":
                    self.score_points(count - 1, 0)
                elif key == "-ANSW2-":
                    self.score_points(count - 1, 1)
                elif key == "-ANSW3-":
                    self.score_points(count - 1, 2)
        print(self.green, self.red, self.blue)

    def score_points(self, count: int, i: int) -> None:
        """Score points based on the selected answer.

        :param count: The current question number
        :type count: int
        :param i: The index of the selected answer
        :type i: int
        """
        color = self.rnd_questions[count].answers[i].type_
        if color == AnswerType.RED:
            self.red += 1
        elif color == AnswerType.GREEN:
            self.green += 1
        else:
            self.blue += 1

    def graphical_result(self) -> None:
        """Display graphical results"""
        res_green = round((self.green * 100) / 15, 1)
        res_red = round((self.red * 100) / 15, 1)
        res_blue = round((self.blue * 100) / 15, 1)

        labels = ["Зеленый", "Красный", "Синий"]
        values = [res_green, res_red, res_blue]
        colors = ["green", "red", "blue"]

        plt.figure(figsize=(9, 6))
        plt.title("Результаты теста", fontsize=20)
        plt.pie(values, labels=labels, autopct="%1.1f%%", colors=colors)
        plt.axis("equal")
        plt.legend(fontsize=14, bbox_to_anchor=(0.8, 1))

        plt.show()

    def text_result(self) -> None:
        """Display text results"""
        green_text = self.loader.read_green_file("green.txt")
        red_text = self.loader.read_red_file("red.txt")
        blue_text = self.loader.read_blue_file("blue.txt")

        title = sg.Text(
            "Зеленный",
            key="-TITLE-",
            font=("Arial", 14),
            pad=((10, 10), (10, 0)),
            text_color="green",
        )
        text = sg.Text(
            green_text, key="-TEXT-", font=("Arial", 12), pad=((10, 10), (10, 0))
        )
        button = sg.Button(
            "Далее",
            enable_events=True,
            key="-FUTHER-",
            font=("Arial", 16),
            pad=((800, 0), (20, 0)),
        )
        layout = [[title], [text], [button]]
        window = sg.Window("Result", layout, size=(950, 550))
        count = 0
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            elif event == "-FUTHER-":
                count += 1
                if count == 1:
                    window["-TITLE-"].update("Красный", text_color="red")
                    window["-TEXT-"].update(red_text)
                elif count == 2:
                    window["-TITLE-"].update("Синий", text_color="blue")
                    window["-TEXT-"].update(blue_text)
                    window["-FUTHER-"].update("Закрыть")
                elif count == 3:
                    break
