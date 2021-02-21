"""File documentation."""

from dragonCurve1 import functioncycle, functionprinttantsrlrl

def test_cycle():
    """Function documentation."""
    assert functioncycle(2) == "rrl"
    assert functioncycle(3) == "rrlrrll"
    assert functioncycle(4) == "rrlrrllrrrllrll"
    assert functioncycle(5) == "rrlrrllrrrllrllrrrlrrlllrrllrll"

def test_print():
    """Function documentation."""
    assert functionprinttantsrlrl("y", "10") == "10"
    assert functionprinttantsrlrl("n", "10") == ""

if __name__ == '__main__':
    test_cycle()
    test_print()
