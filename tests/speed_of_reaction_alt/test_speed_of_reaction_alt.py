import random

from unittest.mock import Mock, call

import pytest

import speed_of_reaction_alt

from speed_of_reaction_alt import (
    RAND_RANGE,
    evaluate_results,
    ask_a_question,
    evaluate_answer,
    generate_question,
    interact_with_user,
    main,
)


def test_main(monkeypatch, capsys):
    monkeypatch.setattr(
        speed_of_reaction_alt,
        "interact_with_user",
        Mock(),
    )
    monkeypatch.setattr(
        speed_of_reaction_alt,
        "ask_a_question",
        Mock(),
    )
    monkeypatch.setattr(
        speed_of_reaction_alt,
        "evaluate_results",
        Mock(
            return_value=(0, 0),
        ),
    )

    main()

    # test if question was asked exactly NUMBER_OF_EXAMPLES times
    assert (
        speed_of_reaction_alt.ask_a_question.call_count
        == speed_of_reaction_alt.NUMBER_OF_EXAMPLES
    )
    # test that the needed report was generated
    assert (
        capsys.readouterr().out
        == "Success rate is: 0\nFor 5 tasks you've spent 0 sec.\n"
    )


@pytest.mark.parametrize(
    (
        "question",
        "type_converter",
        "exp_answer_to_continue",
        "exp_answer_to_quit",
        "number_of_trials",
        "unvalidated_answer",
        "expected_result",
        "expected_exception",
    ),
    (
        # test a normal case
        (
            "anything",
            int,
            None,
            None,
            1,
            "1",
            1,
            None,
        ),
        # check if expected answers functionality works
        (
            "anything",
            str,
            ("Yes",),
            None,
            1,
            "Yes",
            "Yes",
            None,
        ),
        (
            "anything",
            str,
            ("Yes",),
            None,
            1,
            "No",
            None,
            SystemExit,
        ),
        (
            "anything",
            str,
            ("Da", "Ano"),
            None,
            1,
            "Yes",
            None,
            SystemExit,
        ),
        (
            "anything",
            str,
            ("Da", "Ano"),
            None,
            1,
            "Da",
            "Da",
            None,
        ),
        (
            "anything",
            str,
            ("Da", "Ano"),
            None,
            1,
            "Ano",
            "Ano",
            None,
        ),
        (
            "anything",
            str,
            ("Da", "Ano"),
            (
                "Net",
                "Ne",
            ),
            1,
            "Net",
            None,
            SystemExit,
        ),
        (
            "anything",
            str,
            ("Da", "Ano"),
            (
                "Net",
                "Ne",
            ),
            1,
            "Ne",
            None,
            SystemExit,
        ),
        # check type converter works
        (
            "anything",
            "bad_validator",
            ("Da", "Ano"),
            None,
            1,
            "Ano",
            "Ano",
            SystemExit,
        ),
    ),
)
def test_interact_with_the_user(
    monkeypatch,
    question,
    type_converter,
    exp_answer_to_continue,
    exp_answer_to_quit,
    number_of_trials,
    unvalidated_answer,
    expected_result,
    expected_exception,
):
    get_result = lambda: interact_with_user(
        q=question,
        type_converter=type_converter,
        exp_answer_to_continue=exp_answer_to_continue,
        exp_answer_to_quit=exp_answer_to_quit,
        number_of_trials=number_of_trials,
        unvalidated_answer=unvalidated_answer,
    )
    if expected_exception:
        with pytest.raises(expected_exception):
            get_result()
    else:
        assert get_result() == expected_result


def test_generate_question(monkeypatch):
    randint = Mock(return_value=1)
    randchoice = Mock(return_value="+")
    monkeypatch.setattr(random, "randint", randint)
    monkeypatch.setattr(random, "choice", randchoice)

    actual = generate_question()
    assert randint.call_args_list == [call(*RAND_RANGE), call(*RAND_RANGE)]
    assert randchoice.call_count == 1
    assert actual == "1 + 1"


def test_generate_question_0_div(monkeypatch):
    """Test if function properly handles zero division.

    randomint first time returns 0, 0 and on a second call (recursive) returns
    0, 1 and returns the result. We test a proper result and number of random.choice
    is called
    """
    zero_one_it = iter((0, 0, 0, 1))

    def lambda_(*args):
        return next(zero_one_it)

    random_choice = Mock(return_value="/")
    monkeypatch.setattr(random, "randint", lambda_)
    monkeypatch.setattr(random, "choice", random_choice)
    actual = generate_question()
    assert actual == "0 / 1"
    assert random_choice.call_count == 2


@pytest.mark.parametrize(
    ("question", "answer", "expected", "expected_err"),
    (
        ("1 + 1", 2, (True, 2), None),
        ("1 + 1", 3, (False, 2), None),
        ("1 // 1", 3, (False, 2), ValueError),
        ("1+1", 3, (False, 2), ValueError),
        (None, 3, (False, 2), ValueError),
    ),
)
def test_evaluate_answer(
    monkeypatch, question, answer, expected, expected_err
):
    get_actual = lambda: evaluate_answer(question, answer)
    if expected_err:
        with pytest.raises(expected_err):
            get_actual()
    else:
        assert evaluate_answer(question, answer) == expected


@pytest.mark.parametrize(
    ("question", "answer", "expected"),
    (
        ("1 + 1", 2, True),
        ("1 + 1", 3, False),
    ),
)
def test_ask_a_question(monkeypatch, question, answer, expected):
    monkeypatch.setattr(
        speed_of_reaction_alt, "generate_question", Mock(return_value=question)
    )
    monkeypatch.setattr(
        speed_of_reaction_alt, "interact_with_user", Mock(return_value=answer)
    )
    assert ask_a_question() == expected


@pytest.mark.parametrize(
    ("results", "time", "expected", "expected_err"),
    (
        ([True, True], 1, (1.0, 1), None),
        ([True, False], 1, (0.5, 1), None),
        ([False, False], 1, (0, 1), None),
        ([False, False], None, (0, 1), ValueError),
        ([], 1, (0, 1), ValueError),
        (None, 1, (0, 1), ValueError),
    ),
)
def test_evaluate_results(monkeypatch, results, time, expected, expected_err):
    get_actual = lambda: evaluate_results(results, time)
    if expected_err:
        with pytest.raises(expected_err):
            get_actual()
    else:
        assert get_actual() == expected
