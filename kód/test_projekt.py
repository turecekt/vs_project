"""Unitt testy."""

import projekt


def test_dlzkystran():
    """Test pre funkciu dlzkastrany."""
    assert projekt.dlzkastrany(1, 1, 4, 5) == 5.0
    assert projekt.dlzkastrany(1, 1, 2, 1) == 1.0
    assert projekt.dlzkastrany(-3, 1, 4, 1) == 7.0


def test_obvod():
    """Test pre funkciu obvod."""
    assert projekt.obvod(1, 2, 3) == 6
    assert projekt.obvod(5, 4, 2) == 11
    assert projekt.obvod(12, 23, 30) == 65
    assert projekt.obvod(8, 8, 8) == 24


def test_obsah():
    """Test pre funkciu obsah."""
    assert projekt.obsah(4, 5, 6) == 9.9216
    assert projekt.obsah(1, 1, 1) == 0.433


def test_zostrojenost():
    """Test pre funkciu zostrojenost."""
    assert projekt.zostrojenost(3, 4, 5) == 1
    assert projekt.zostrojenost(1, 5, 10) == 0
    assert projekt.zostrojenost(1, 2, 3) == 0


def test_pravouhlost():
    """Test pre funkciu pravouhlost."""
    assert projekt.pravouhlost(3, 4, 5) == 1
    assert projekt.pravouhlost(4, 4, 4) == 0
    assert projekt.pravouhlost(7, 9, 16) == 0


if __name__ == '__main__':
    test_dlzkystran()
    test_obvod()
    test_obsah()
    test_zostrojenost()
    test_pravouhlost()
