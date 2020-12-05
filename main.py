"""Search all relevant links got from the URL address.

This is proof of concept. In the future, this code can by using as
part of crawlers, web site checkers or generator sitemap, etc.

Usage:
    python3 -i <starturl> for search links
    python3 -h for help
Example:
  python3 main.py -i https://seznam.cz
"""

# Author:   Michal Raška <m_raska@utb.cz>
#           Roman Mareček <r_marecek@utb.cz>
#
# License:

import sys
import getopt  # for parse input args
import links
import connector

# TODO move to separate class in future


def coreParser(url):
    """Parse html code for links.

    Args:
        - url - The URL address for parsing example http://example.com

    Returns:
        - output - Reference at link object which
                   has an array with links.
    """
    connect = connector.Connector(url)
    dataDirty = connect.getWebData()

    link = links.Links()
    link.findLinks(dataDirty)

    return link


def main(argv):
    """Entry point for the program.

    Args:
        - argv - inline parameter

    Returns:
        - output - Print links on the web page.
    """
    url = ""

    try:
        opts, args = getopt.getopt(argv, "hi:", ["iurl="])
    except getopt.GetoptError:
        print('main.py -i <startURL>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <starturl>')
            sys.exit()
        elif opt in ("-i", "--iurl"):
            url = arg

    link = coreParser(url)

    print(link.links)
    print(link.linksCount)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
