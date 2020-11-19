# usage python3 -i <starturl> for search links
#       python# -h for help
# example python3 main.py -i https://seznam.cz

import sys
import getopt  # for parse input args
import links
import connector
import sqlite3


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

    connect = connector.Connector(url)
    dataDirty = connect.getWebData()

    link = links.Links()
    link.findLinks(dataDirty)

    # TODO store urls into SQLITe DB.
    conn = sqlite3.connect('crawler.db')
    c = conn.cursor()

    # print(dataDirty)
    print(len(dataDirty))
    print(link.links)
    print(link.linksCount)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
