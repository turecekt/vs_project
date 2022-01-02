#### testovani funkcionalit #####
import unittest
#prozatim import touto cestou nez bude venv
"""import importlib.util
spec = importlib.util.spec_from_file_location("CetnostZnaku", "C:/01_Batovka/AK1VS/vs_project/Project/CetnostZnaku.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
"""
import CetnostZnaku
def test_secti():
    assert secti(1,2) == 3
"""
def test_CheckVstup():
    assert foo.CheckVstup('Vstup #'.endswith('#'))
"""
    
    