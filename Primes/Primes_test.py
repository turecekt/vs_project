"""Pytest pro Primes.py."""

from Primes import VolbaAkce, OvereniHodnotyAkce
from Primes import VolbaCisla, OvereniHodnotyCisla
from Primes import Determinacni, Fermat
from Primes import UrciPrvocislo, VypisPrvocisel, ProvedAkci


def test_VolbaAkce():
    """Test pro metodu VolbaAkce."""
    pass


def test_OvereniHodnotyAkce():
    """Test pro metodu OvereniHodnotyAkce."""
    assert OvereniHodnotyAkce(1) is True
    assert OvereniHodnotyAkce(2) is True
    assert OvereniHodnotyAkce("abc") is False


def test_VolbaCisla():
    """Test pro metodu VolbaCisla."""
    pass


def test_OvereniHodnotyCisla():
    """Test pro metodu OvereniHodnotyCisla."""
    assert OvereniHodnotyCisla(100) is True
    assert OvereniHodnotyCisla(-50) is False
    assert OvereniHodnotyCisla("abc") is False


def test_Determinacni():
    """Test pro metodu Determinacni."""
    assert Determinacni(421) is True
    assert Determinacni(12) is False
    assert Determinacni(1) is True


def test_Fermat():
    """Test pro metodu Fermat."""
    assert Fermat(1421) is False
    assert Fermat(421) is True
    assert Fermat(11) is True


def test_UrciPrvocislo():
    """Test pro metodu UrciPrvocislo."""
    pass


def test_VypisPrvocisel():
    """Test pro metodu VypisPrvocisel."""
    pass
