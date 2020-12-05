"""Tests for example."""

# Author:   Michal Raška <m_raska@utb.cz>
#           Roman Mareček <r_marecek@utb.cz>
#
# License:

import links
import connector
import main

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


# required new instance for next test
link1 = links.Links()


def test_clearStoredLinks():
    """Test clearing stored links."""
    testTextWithLink = "Totoje proste test <a href=\"http://example.com\">  " \
                       "</a>"

    link1.findLinks(testTextWithLink)
    link1.clearStoredLinks()
    assert (link1.linksCount == 0)
    assert (len(link1.links) == 0)


def test_findLinks():
    """Test to find the target URL."""
    testText = "Totoje proste test"
    link1.findLinks(testText)
    assert (link1.linksCount == 0)

    # Testfor onelink
    link1.clearStoredLinks()
    testTextWithLink = "Totoje proste test <a href=\"http://example.com\">  " \
                       "example.com </a>"
    link1.findLinks(testTextWithLink)
    assert (link1.linksCount == 1)
    link1.clearStoredLinks()

    # Test for two links
    testTextTwoLink = "Totoje proste test <a href=\"http://example.com\"> " \
                      "example.com </a> <a href=\"https://seznam.cz\">  " \
                      "seznam.cz </a> that's all."
    link1.findLinks(testTextTwoLink)
    assert (link1.linksCount == 2)
    assert (link.links[0] == "http://example.com")
    assert (link.links[1] == "https://seznam.cz")
    assert (len(link.links) == 2)


# *********** Modul connector  ***********


url = "http://example.com"
conn = connector.Connector(url)


def test_init():
    """Test for store URL address into a class variable URL."""
    assert (conn.url == "http://example.com")


def test_getWebData():
    """Test for proper output from the example."""
    fd = open("index.html", "r")
    if fd is None:
        print("File index.html not found")
        exit(-1)
    else:
        htmlData = fd.read()
        assert (conn.getWebData() == htmlData.lower())


# *********** Main  ***********


def test_main():
    """Test for proper output from the example."""
    link = main.coreParser(url)
    linkCount = len(link.links)

    assert (linkCount == 3)
    assert (link.links[2] == "https://www.iana.org/domains/example")
