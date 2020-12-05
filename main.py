# usage python3 -i <starturl> for search links
#       python# -h for help
# example python3 main.py -i https://seznam.cz


# Author:   Michal Raška <m_raska@utb.cz>
#           Roman Mareček <r_marecek@utb.cz>
#
# License:

import sys
import getopt  # for parse input args
import links
import connector




def coreParser(url):

    connect = connector.Connector(url)
    dataDirty = connect.getWebData()

    link = links.Links()
    link.findLinks(dataDirty)
    return link


def main(argv):
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
