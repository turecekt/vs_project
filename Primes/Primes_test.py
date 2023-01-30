"""Pytest pro Primes.py."""

from Primes import VolbaAkce, OvereniHodnotyAkce
from Primes import VolbaCisla, OvereniHodnotyCisla
from Primes import Determinacni, Fermat
from unittest import mock


@mock.patch('Primes.input', return_value=1)
def test_VolbaAkce(mock_akce):
    """Test pro metodu VolbaAkce."""
    assert VolbaAkce() == 1


def test_OvereniHodnotyAkce():
    """Test pro metodu OvereniHodnotyAkce."""
    assert OvereniHodnotyAkce(1) is True
    assert OvereniHodnotyAkce(2) is True
    assert OvereniHodnotyAkce("abc") is False


@mock.patch('Primes.input', return_value=10)
def test_VolbaCisla(mock_zadanecislo):
    """Test pro metodu VolbaCisla."""
    assert VolbaCisla() == 10


def test_OvereniHodnotyCisla():
    """Test pro metodu OvereniHodnotyCisla."""
    assert OvereniHodnotyCisla(100) is True
    assert OvereniHodnotyCisla(-50) is False
    assert OvereniHodnotyCisla("abc") is False


def test_Determinacni():
    """Test pro metodu Determinacni."""
    assert Determinacni(421) is True
    assert Determinacni(12) is False
    assert Determinacni(1) is False


def test_Fermat():
    """Test pro metodu Fermat."""
    assert Fermat(1421) is False
    assert Fermat(1033) is True
    assert Fermat(11) is True
