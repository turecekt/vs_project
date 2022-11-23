from unidecode import unidecode
import pytest

import morse
from morse import encode
from morse import decode


def test_encode():
    assert encode("A") == ".-/"


def test_decode():
    assert decode(".-") == "A"

