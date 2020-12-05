"""Tests for example."""

# Author:   Michal Raška <m_raska@utb.cz>
#           Roman Mareček <r_marecek@utb.cz>
#
# License:

import links

# *********** Modul links  ***********

link = links.Links()


def test_findAnchor():
    """Test for search <a as beginning HTML anchor."""
    testText = "Totoje proste test"
    assert (link.findAnchor(testText + " <a href=...", 0) == 19)


def test_findTargetURL():
    """Test to find the target URL."""
    testText = "Totoje proste test"
    assert (link.findTargetURL(0, testText))
    assert (link.findTargetURL(-1, testText) == -1)
