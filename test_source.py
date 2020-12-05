"""Tests for example."""

# Author:   Michal Raška <m_raska@utb.cz>
#           Roman Mareček <r_marecek@utb.cz>
#
# License:

import links
import connector

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

# *********** Modul connector  ***********


url = "http://example.com"
conn = connector.Connector(url)


def test_init():
    """Test for store URL address into a class variable URL."""
    assert (conn.url == "http://example.com")
