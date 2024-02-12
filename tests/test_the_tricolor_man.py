import pytest
from app import Test, Answer, AnswerType, Question


@pytest.fixture
def test_object():
    test = Test("test.txt")
    return test


def test_initialization(test_object):
    assert test_object.loader is not None
    assert test_object.rnd_questions is not None
    assert test_object.green == 0
    assert test_object.red == 0
    assert test_object.blue == 0


def test_random_questions(test_object):
    test_object.random_questions()
    assert test_object.rnd_questions is not None
    assert test_object.rnd_questions != test_object.loader.read_test_file()


def test_determining_answer(test_object):
    values1 = {"-ANSW1-": True, "-ANSW2-": False, "-ANSW3-": False}
    test_object.determining_answer(values1, 1)
    assert test_object.green == 1
    assert test_object.red == 0
    assert test_object.blue == 0

    values2 = {"-ANSW1-": False, "-ANSW2-": True, "-ANSW3-": False}
    test_object.determining_answer(values2, 1)
    assert test_object.green == 1
    assert test_object.red == 0
    assert test_object.blue == 1

    values3 = {"-ANSW1-": False, "-ANSW2-": False, "-ANSW3-": True}
    test_object.determining_answer(values3, 1)
    assert test_object.green == 1
    assert test_object.red == 1
    assert test_object.blue == 1


def test_graphical_result(test_object, mocker):
    mock_show = mocker.patch("matplotlib.pyplot.show")
    test_object.green = 2
    test_object.red = 3
    test_object.blue = 4
    test_object.graphical_result()
    assert mock_show.called


def test_str_question():
    question = Question(
        "вопрос?",
        [
            Answer(AnswerType.RED, "ответ1"),
            Answer(AnswerType.GREEN, "ответ2"),
            Answer(AnswerType.BLUE, "ответ3"),
        ],
    )
    assert (
        question.__str__()
        == "Question: вопрос?\nAnswer: ответ1 AnswerType.RED\nAnswer: ответ2 AnswerType.GREEN\nAnswer: ответ3 AnswerType.BLUE"
    )


def test_read_color_file(test_object):
    text_green = test_object.loader.read_green_file("test_text.txt")
    text_red = test_object.loader.read_red_file("test_text.txt")
    text_blue = test_object.loader.read_blue_file("test_text.txt")
    text = "Синий – человек холодный, расчетливый, осторожный и предпочитает держаться от всего на расстоянии."
    assert text_green == text
    assert text_red == text
    assert text_blue == text


def test_raises_read_test_file():
    with pytest.raises(FileNotFoundError):
        Test("ttt.txt")


def test_raises_read_green_file(test_object):
    with pytest.raises(FileNotFoundError):
        test_object.loader.read_green_file("ttt.txt")


def test_raises_read_red_file(test_object):
    with pytest.raises(FileNotFoundError):
        test_object.loader.read_red_file("ttt.txt")


def test_raises_read_blue_file(test_object):
    with pytest.raises(FileNotFoundError):
        test_object.loader.read_blue_file("ttt.txt")


def test_checking_answer_selected():
    assert (
        Test.checking_answer_selected(
            {"answ1": False, "answ2": True, "answ3": False}
        )
        == True
    )




