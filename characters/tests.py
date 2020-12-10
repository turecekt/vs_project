"""Unit tests."""

import soubor

def test_fileExists():
    """fileExists Unit Test."""
    text = "ahoj"
    actual = soubor.fileExists("ahoj.txt")
    assert(actual == text)
    
if __name__ == "__main__":
    print("running")