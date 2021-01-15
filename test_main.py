# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:45:18 2021.

@author: adtom
"""
import math
from main import toNumber, Uprava_jednotek, Tris


class Test():
    """Trida pro unit testy."""

    def test_toNumber(self):
        """Testuje funkci toNumber()."""
        test = "2**5"
        result = 32
        test = toNumber(test)
        assert test == result
        test = "sqrt(625)"
        result = 25
        test = toNumber(test)
        assert test == result
        test = "(5+3)/2"
        result = 4
        test = toNumber(test)
        assert test == result

    def test_tris_sss(self):
        """Testuje třídu Tris(), pro trojúhelník sss."""
        test = {0: ('500', 'cm'),
                1: ('40', 'dm'),
                2: ('3', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = {0: 'strana a – 5.0m',
                  1: 'strana b – 4.0m',
                  2: 'strana c – 3.0m',
                  3: 'úhel α – 1.5708rad, 90.0°',
                  4: 'úhel β – 0.9273rad, 53.1301°',
                  5: 'úhel γ – 0.6435rad, 36.8699°',
                  6: 'výška a – 2.4m',
                  7: 'výška b – 3.0m',
                  8: 'výška c – 4.0m',
                  9: 'obvod  – 12.0m',
                  10: 'obsah – 6.0m²',
                  11: 'typ – pravoúhlý'}
        test = Tris(test)
        assert test.result == result

    def test_tris_sss_2(self):
        """Testuje třídu Tris(), pro trojúhelník sss."""
        test = {0: ('500', 'cm'),
                1: ('40', 'dm'),
                2: ('3', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = {0: 'strana a – 5.0m',
                  1: 'strana b – 4.0m',
                  2: 'strana c – 3.0m',
                  3: 'úhel α – 1.5708rad, 90.0°',
                  4: 'úhel β – 0.9273rad, 53.1301°',
                  5: 'úhel γ – 0.6435rad, 36.8699°',
                  6: 'výška a – 2.4m',
                  7: 'výška b – 3.0m',
                  8: 'výška c – 4.0m',
                  9: 'obvod  – 12.0m',
                  10: 'obsah – 6.0m²',
                  11: 'typ – pravoúhlý'}
        test = Tris(test)
        assert test.tris_sss() == result

    def test_tris_sus(self):
        """Testuje třídu Tris(), pro trojúhelník sus."""
        test = {0: ('', ''),
                1: ('40', 'dm'),
                2: ('3', 'm'),
                3: ('2**6', '°'),
                4: ('', ''),
                5: ('', '')}
        result = {0: 'strana a – 38.0514dm',
                  1: 'strana b – 40dm',
                  2: 'strana c – 30dm',
                  3: 'úhel α – 1.11701rad, 64.0°',
                  4: 'úhel β – 1.23705rad, 70.8776°',
                  5: 'úhel γ – 0.78753rad, 45.1224°',
                  6: 'výška a – 28.34463dm',
                  7: 'výška b – 26.96382dm',
                  8: 'výška c – 35.95176dm',
                  9: 'obvod  – 108.0514dm',
                  10: 'obsah – 539.28dm²',
                  11: 'typ – obecný'}
        test = Tris(test)
        assert test.result == result

    def test_tris_sus_2(self):
        """Testuje třídu Tris(), pro trojúhelník sus."""
        test = {0: ('', ''),
                1: ('40', 'dm'),
                2: ('3', 'm'),
                3: ('2**6', '°'),
                4: ('', ''),
                5: ('', '')}
        result = {0: 'strana a – 38.0514dm',
                  1: 'strana b – 40dm',
                  2: 'strana c – 30dm',
                  3: 'úhel α – 1.11701rad, 64.0°',
                  4: 'úhel β – 1.23705rad, 70.8776°',
                  5: 'úhel γ – 0.78753rad, 45.1224°',
                  6: 'výška a – 28.34463dm',
                  7: 'výška b – 26.96382dm',
                  8: 'výška c – 35.95176dm',
                  9: 'obvod  – 108.0514dm',
                  10: 'obsah – 539.28dm²',
                  11: 'typ – obecný'}
        test = Tris(test)
        assert test.tris_sus() == result

    def test_tris_usu(self):
        """Testuje třídu Tris(), pro trojúhelník sus."""
        test = {0: ('', ''),
                1: ('40', 'cm'),
                2: ('', ''),
                3: ('2**6', '°'),
                4: ('', ''),
                5: ('1', 'rad')}
        result = {0: 'strana a – 42.07359cm',
                  1: 'strana b – 40cm',
                  2: 'strana c – 39.39023cm',
                  3: 'úhel α – 1.11701rad, 64.0°',
                  4: 'úhel β – 1.02458rad, 58.70422°',
                  5: 'úhel γ – 1rad, 57.29578°',
                  6: 'výška a – 33.65884cm',
                  7: 'výška b – 35.40371cm',
                  8: 'výška c – 35.95176cm',
                  9: 'obvod  – 121.46382cm',
                  10: 'obsah – 708.07cm²',
                  11: 'typ – obecný'}
        test = Tris(test)
        assert test.result == result

    def test_tris_usu_2(self):
        """Testuje třídu Tris(), pro trojúhelník sus."""
        test = {0: ('', ''),
                1: ('40', 'cm'),
                2: ('', ''),
                3: ('2**6', '°'),
                4: ('', ''),
                5: ('1', 'rad')}
        result = {0: 'strana a – 42.07359cm',
                  1: 'strana b – 40.0cm',
                  2: 'strana c – 39.39023cm',
                  3: 'úhel α – 1.11701rad, 64.0°',
                  4: 'úhel β – 1.02458rad, 58.70422°',
                  5: 'úhel γ – 1.0rad, 57.29578°',
                  6: 'výška a – 33.65884cm',
                  7: 'výška b – 35.40371cm',
                  8: 'výška c – 35.95176cm',
                  9: 'obvod  – 121.46382cm',
                  10: 'obsah – 708.07cm²',
                  11: 'typ – obecný'}
        test = Tris(test)
        assert test.tris_usu() == result

    def test_tris_error(self):
        """Testuje třídu Tris(), pro error."""
        test = {0: ('20', 'dm'),
                1: ('40', 'cm'),
                2: ('5', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = "Nejedná se o trojúhelník.\n"
        result += "Součet dvou stran musí být větší než strana třetí.\n"
        result += "Součet dvou úhlů musí být menší než 180\xb0 nebo "
        result += "\u03C0 rad. Nejmenší možný úhel je 0,013\xb0"
        test = Tris(test)
        assert test.result == result

    def test_tris_error_2(self):
        """Testuje třídu Tris(), pro error."""
        test = {0: ('20', 'dm'),
                1: ('40', 'cm'),
                2: ('5', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = "Nejedná se o trojúhelník.\n"
        result += "Součet dvou stran musí být větší než strana třetí.\n"
        result += "Součet dvou úhlů musí být menší než 180\xb0 nebo "
        result += "\u03C0 rad. Nejmenší možný úhel je 0,013\xb0"
        test = Tris(test)
        assert test.output() == result

    def test_tris_error_3(self):
        """Testuje třídu Tris(), pro error."""
        test = {0: ('20', 'dm'),
                1: ('40', 'cm'),
                2: ('5', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = "Nejedná se o trojúhelník.\n"
        result += "Součet dvou stran musí být větší než strana třetí.\n"
        result += "Součet dvou úhlů musí být menší než 180\xb0 nebo "
        result += "\u03C0 rad. Nejmenší možný úhel je 0,013\xb0"
        test = Tris(test)
        assert test.__str__() == result

    def test_is_tris_S(self):
        """Testuje metodu is tris s."""
        test = {0: ('30', 'dm'),
                1: ('400', 'cm'),
                2: ('5', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = True
        test = Tris(test)
        assert test.is_tris_S() == result

    def test_is_tris_U(self):
        """Testuje metodu is tris u."""
        test = {0: ('', ''),
                1: ('', ''),
                2: ('', ''),
                3: ('3', 'rad'),
                4: ('2', 'rad'),
                5: ('0', '°')}
        result = False
        test = Tris(test)
        assert test.is_tris_U() == result

    def test_is_tris(self):
        """Testuje metodu is tris."""
        test = {0: ('30', 'dm'),
                1: ('400', 'cm'),
                2: ('5', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = True
        test = Tris(test)
        assert test.is_tris() == result

    def test_cos_veta(self):
        """Testuje metodu cos veta."""
        test = {0: ('30', 'dm'),
                1: ('400', 'cm'),
                2: ('5', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = math.pi / 2
        test = Tris(test)
        assert test.cos_veta("uC") == result

    def test_sin_veta(self):
        """Testuje metodu sin veta."""
        test = {0: ('30', 'dm'),
                1: ('300', 'cm'),
                2: ('', ''),
                3: ('', ''),
                4: ('60', '°'),
                5: ('', '')}
        result = round((math.pi / 3), 8)
        test = Tris(test)
        assert round(test.sin_veta("uA"), 8) == result

    def test_to_rad(self):
        """Testuje převod na radiany."""
        test = Uprava_jednotek().to_rad(u1=360, uhel1="°")
        result = math.pi * 2
        assert test == result

    def test_prevod_delky(self):
        """Testuje metodu prevod delky."""
        tmp = Uprava_jednotek(sA=5, sB=55, sC=300, unsA="m", unsB="dm",
                              unsC="cm")
        tmp.prevod_delky()
        test = {1: (tmp.sA, tmp.unsA),
                2: (tmp.sB, tmp.unsB),
                3: (tmp.sC, tmp.unsC)}
        result = {1: (500, 'cm'),
                  2: (550, 'cm'),
                  3: (300, 'cm')}
        assert test == result

    def test_int_to_delka(self):
        """Testuje metodu int to delka."""
        test = Uprava_jednotek(unsA=1)
        result = "mm"
        assert test.int_to_delka(test.unsA) == result

    def test_delka_to_int(self):
        """Testuje metodu delka to int."""
        test = Uprava_jednotek(unsA="m")
        result = 4
        assert test.delka_to_int(test.unsA) == result

    def test_dve_strany(self):
        """Testuje metodu dve strany."""
        test = Uprava_jednotek(sA=5, sB=55, unsA="m", unsB="dm")
        result = ('dm', 'dm', 50, 55)
        assert test.dve_strany(test.unsA, test.unsB, test.sA,
                               test.sB) == result

    def test_uhel_to_int(self):
        """Testuje metodu uhel to int."""
        test = Uprava_jednotek(unuC="°")
        result = 1
        assert test.uhel_to_int(test.unuC) == result

    def test_int_to_uhel(self):
        """Testuje metodu int to uhel."""
        test = Uprava_jednotek(unuC=2)
        result = "rad"
        assert test.int_to_uhel(test.unuC) == result

    def test_draw(self):
        """Testuje metodu draw."""
        test = {0: ('30', 'dm'),
                1: ('400', 'cm'),
                2: ('5', 'm'),
                3: ('', ''),
                4: ('', ''),
                5: ('', '')}
        result = (645.6496908383268, 53.13010235415599, 387.3898145029961,
                  90.0, 516.5197526706612, 36.86989764584401,
                  309.91185160239695)
        test = Tris(test)
        assert test.draw() == result
