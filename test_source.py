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
