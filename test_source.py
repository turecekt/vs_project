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
    testTextNoLink = "Totoje proste test"
    testTextWithLink = "Totoje proste test <a href=\"http://example.com\">  " \
                       "example.com </a>"
    # test for index after url
    assert (link.findTargetURL(0, testTextWithLink) == 46)
    # test for found link
    assert (link.links[0] == "http://example.com")
    # test there are only one link
    assert (len(link.links) == 1)
    # there are not a link
    assert (link.findTargetURL(-1, testTextNoLink) == -1)


# *********** Modul connector  ***********


url = "http://example.com"
conn = connector.Connector(url)


def test_init():
    """Test for store URL address into a class variable URL."""
    assert (conn.url == "http://example.com")