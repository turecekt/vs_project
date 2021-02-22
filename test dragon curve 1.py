"""Unit tests for dragon Curve functions."""

from dragonCurve1 import functioncycle, functionprinttantsrlrl


def test_cycle():

"""Test of cycle"""
    assert functioncycle(2) == "rrl"
    assert functioncycle(3) == "rrlrrll"
    assert functioncycle(4) == "rrlrrllrrrllrll"
    assert functioncycle(5) == "rrlrrllrrrllrllrrrlrrlllrrllrll"

def test_print():
    
    """Test of Lsystem form"""
    assert functionprinttantsrlrl("y", "10") == "10"
    assert functionprinttantsrlrl("n", "10") == ""

    
if __name__ == '__main__':
    test_cycle()
    test_print()
