"""Testování modulu example."""
import trojuhelnik


def test_is_valid():
    """Test vyhodnocení bodů na jedné přímce jako False."""
    assert trojuhelnik.sestrojitelnost([(0, 0), (0, 4), (0, -2)]) is False
    assert trojuhelnik.sestrojitelnost([(0, 0), (3, 0), (0, -2)]) is True


def test_side_lengths():
    """Test výpočtu délek stran."""
    assert trojuhelnik.delky_stran([(0, 0), (3, 0), (0, 4)]) == [5, 4, 3]
    assert trojuhelnik.delky_stran([(0, 0), (-3, 0), (0, -4)]) == [5, 4, 3]


def test_side_stats():
    """Test výpočtu délek stran."""
    assert trojuhelnik.serad_strany([(0, 0), (3, 0), (0, 4)]) == [5, 4, 3]
    assert trojuhelnik.serad_strany([(0, 0), (-3, 0), (0, -4)]) == [5, 4, 3]
    assert trojuhelnik.serad_strany([(-3, 0), (0, -4), (0, 0)]) == [5, 4, 3]


def test_circumference():
    """Test výpočtu obvodu stran."""
    assert trojuhelnik.obvod([(0, 0), (3, 0), (0, 4)]) == 12
    assert trojuhelnik.obvod([(0, 0), (-3, 0), (0, -4)]) == 12


def test_area():
    """Test výpočtu obvodu stran."""
    assert trojuhelnik.obsah([(0, 0), (3, 0), (0, 4)]) == 6
    assert trojuhelnik.obsah([(0, 0), (-3, 0), (0, -4)]) == 6


def test_is_right():
    """Test určení pravoúhlého trojuhelníku."""
    assert trojuhelnik.pravouhlost([(0, 0), (3, 0), (0, 4)]) is True
    assert trojuhelnik.pravouhlost([(0, 0), (3, 2), (1, 4)]) is False
