"""module links.

The module is used for working with an HTML link
"""


# Author:   Michal Raška <m_raska@utb.cz>
#           Roman Mareček <r_marecek@utb.cz>
#
# License:


class Links:
    """Class for searching links from the HTML code."""

    url = ''
    links = []
    linksCount = 0

    def findAnchor(self, data, offset):

        # high speed, but dumb way
        lenght = len(data)

        index = data.find('<a', offset, lenght)
        return index

    def findTargetURL(self, offset, data):

        if offset < 0:
            return -1

        # return value is url
        url = ""

        # no find over lenght
        lenght = len(data)

        index = data.find('href', offset, lenght)

        i = index

        # after href must be '='
        while data[i] != '=':
            i = i + 1
            if i >= lenght:
                # no way
                i = -1
                return i

        # in next find " or '

        while data[i] != "\"" and (data[i] != "\'"):
            i = i + 1
            if i >= lenght:
                i = -1
                return i

        # ok and add char to url string while not find ' or "
        # i point to finded " or ' must be skipped

        i = i + 1

        # counter for url string

        while data[i] != '"' and data[i] != "'" and data[i] != ' ':
            url = url + data[i]
            i = i + 1

            if i >= lenght:
                i = -1
                url = ""
                break

        if url.find('http://') != -1 \
                or url.find('https://') != -1 \
                or url.find('/', 0, 1) != -1:
            self.links.append(url)
            self.linksCount = self.linksCount + 1

        return i

    def findLinks(self, data):
        lenght = len(data)
        i = 0
        while i < lenght and i != -1:
            i = self.findTargetURL(self.findAnchor(data, i), data)
