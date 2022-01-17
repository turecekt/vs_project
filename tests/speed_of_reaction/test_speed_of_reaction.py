import pytest

from _pytest.monkeypatch import MonkeyPatch
from pytest_mock import MockerFixture

import speed_of_reaction

from speed_of_reaction import main


@pytest.mark.parametrize(
    ("questions", "answers", "exp_success_ratio"),
    (
        (((1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3)), (2, 0, 1, 1), "4/4"),
        (((1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 1, 3)), (1, 0, 1, 1), "3/4"),
    ),
)
def test_main(
    monkeypatch: MonkeyPatch,
    mocker: MockerFixture,
    capsys,
    answers,
    questions,
    exp_success_ratio,
):
    answers_iter = iter(answers)
    questions_iter = iter(questions)
    mocked_questions = mocker.Mock(side_effect=lambda: next(questions_iter))
    mocked_answers = mocker.Mock(side_effect=lambda: str(next(answers_iter)))
    monkeypatch.setattr(
        speed_of_reaction,
        "generate_equation",
        mocked_questions,
    )
    monkeypatch.setattr(
        speed_of_reaction,
        "ask_for_answer",
        mocked_answers,
    )
    main(4)
    out, err = capsys.readouterr()
    assert f"Correct answers {exp_success_ratio}" in out
