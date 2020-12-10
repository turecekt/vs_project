"""Unit tests."""

import soubor


def test_fileExists():
    """Fileexists unit test."""
    text = "ahoj"
    actual = soubor.fileExists("ahoj.txt")
    assert(actual.read() == text)


if __name__ == "__main__":
    print("running")
