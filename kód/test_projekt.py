"""Unit testy."""

import projekt


def test_dlzkystran():
    """Test pre funkciu dlzkastrany."""
    assert projekt.dlzkastrany(1, 1, 4, 5) == 5.0


def test_obvod():
    """Test pre funkciu obvod."""
    assert projekt.obvod(1, 2, 3) == 6


def test_obsah():
    """Test pre funkciu obsah."""
    assert projekt.obsah(4, 5, 6) == 9.9216
    assert projekt.obsah(1, 1, 1) == 0.433


def test_zostrojenost():
    """Test pre funkciu zostrojenost."""
    assert projekt.zostrojenost(3, 4, 5) == 1


def test_pravouhlost():
    """Test pre funkciu pravouhlost."""
    assert projekt.pravouhlost(3, 4, 5) == 1
