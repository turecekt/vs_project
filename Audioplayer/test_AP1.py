import unittest
from pygame import mixer
from pygame.compat import unicode_
from pygame.tests.test_utils import example_path
import os


class TestMusicPlayer(unittest.TestCase):
    def test_sound_unicode(self):
        """test non-ASCII unicode path"""
        #Zacatek inicalizaci
        mixer.init()

        import shutil
        # Modul shutil nabizi radu operaci na vysoke urovni se soubory a sbirkami souboru.
        # Konkretne jsou k dispozici funkce podporujici kopirovini a mazini souboru.

        ep = unicode_(example_path('data'))

        temp_file = os.path.join(ep, u'你好.wav')
        org_file = os.path.join(ep, u'house_lo.wav')
        # metoda path.join sdruzuje ruzne komponenty cesty s presne jednim
        # oddelovacem adresaru ( ' / ' ) po kazde neprazdne casti s vyjimkou komponenty posledni cesty.

        shutil.copy(org_file, temp_file)
        # kopiruje soubory org_file, temp_file
        try:
        # Pokus otevreni soubpru
            with open(temp_file, 'rb'):
                # vynechani
                pass
        except IOError:
            # Pri objevovani vyjimky IOError se objevuje unittest.SkipTest,
            # ktery zastavuje test a napise 'the path cannot be opened'.
            raise unittest.SkipTest('the path cannot be opened')
        try:
            sound = mixer.Sound(temp_file)
            del sound
        finally:
            os.remove(temp_file)

    def test_init__zero_values(self):
        # Kontroluje, zda vstupni podminky jsou ekvivalentni.
        mixer.pre_init(44100, 8, 1)
        mixer.init(0, 0, 0)
        self.assertNotEqual(mixer.get_init(), (44100, 8, 1))        

    def test_get_num_channels__defaults_eight_after_init(self):
        # Porovnani poctu zvukovych kanalu v mixer.get_num_channels() s ocekavanymi 8 kanaly.
        mixer.init()
        self.assertEqual(mixer.get_num_channels(), 8)


if __name__ == "__main__":
    unittest.main()
