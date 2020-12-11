"""Modul Test_main."""
import main


def test_nacti_text_seZnakem():
    """Funkce testuje načítání textu ze souboru po znak "#".

    Args:
        - nazev_souboru - Soubor formátu .txt, který chceme načítst

    Returns:
        - obsah - Vrací string
    """
    assert main.nacti_text('basnicka_seznakem.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí'   # noqa


def test_nacti_text_bezZnaku():
    """Funkce testuje načítání textu ze souboru.

    Args:
        - nazev_souboru - Soubor formátu .txt, který chceme načítst

    Returns:
        - obsah - Vrací string
    """
    assert main.nacti_text('basnicka_bezznaku.txt') == 'Ahoj Toto je ta básnička kde končí text a vlastně nikde text nekončí a tady už nám text končí a už dál vlastně vůbec nepokračuje.'  # noqa


def test_nacti_text_znakNaZacatku():
    """Funkce testuje načítání ze souboru, když je znak # jako první.

    Args:
        - nazev_souboru - Soubor formátu .txt, který chceme načítst

    Returns:
        - obsah - null
    """
    assert main.nacti_text('basnicka_nazacatku.txt') == None    # noqa


def test_uprav_text():
    """Funkce testuje převod písmen na malá a odstranění mezer.

    Args:
        - text - Vstup je string, který chceme upravit

    Returns:
        - text - Vrací upravený string
    """
    assert main.uprav_text('Toto je   básnička.') == 'totojebásnička.'


def test_zjisti_cetnosti():
    """Funkce testuje zjišťování četností jednotlivých znaků z textu.

    Args:
        - text - String ve kterém zjišťujeme četnosti znaků

    Returns:
        - count - Vrací četnosti (dictionary)
    """
    assert main.zjisti_cetnosti('basnicka_ha.txt') == {'h': 3, 'a': 3}


def test_pocet_ruznych_znaku():
    """Funkce testuje vrácení počtu různých znaků.

    Args:
        - slovnik - četnosti (dictionary)

    Returns:
        - pocty - počet znaků
    """
    assert main.pocet_ruznych_znaku([('a', 5), ('b', 3), ('c', 1)]) == 3


def test_nejcetnejsi_znaky():
    """Funkce testuje vrácení nejčetnějšího znaku.

    Args:
        - slovnik - četnosti (dictionary)

    Returns:
        - MaxDictVal - nejčetnější znak (string)
    """
    assert main.nejcetnejsi_znaky({'h': 3, 'a': 2}) == 'h'


def test_nejcetnejsi_znaky_2stejne():
    """Funkce testuje vrácení nejčetnějšího znaku v případě 2 stejně četných.

    Args:
        - slovnik - četnosti (dictionary)

    Returns:
        - MaxDictVal - nejčetnější znak (string)
    """
    assert main.nejcetnejsi_znaky({'h': 3, 'a': 2, 'c': 3}) == 'h'


def test_nejmenecetne_znaky():
    """Funkce testuje vrácení nejméně četného znaku.

    Args:
        - slovnik - četnosti (dictionary)

    Returns:
        - MinDictVal - nejméně četný znak (string)
    """
    assert main.nejmenecetne_znaky({'h': 3, 'a': 2}) == 'a'


def test_nejmenecetne_znaky_2stejne():
    """Funkce testuje vrácení nejméně četného znaku v případě 2 stejně četných.

    Args:
        - slovnik - četnosti (dictionary)

    Returns:
        - MinDictVal - nejméně četný znak (string)
    """
    assert main.nejmenecetne_znaky({'h': 3, 'a': 2, 'd': 2}) == 'a'
