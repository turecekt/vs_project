"""Module connector.

The module is used for connecting and transferring data from web servers.
"""

# Author:   Michal Raška <m_raska@utb.cz>
#           Roman Mareček <r_marecek@utb.cz>
#
# License:

import requests


class Connector:
    """Class for downloading a web page in text form."""

    url = ''

    def __init__(self, seedUrl):
        """Construct object and store URL into internal storage.

        Args:
            - seedUrl - URL address

        Returns:
            - output - None
        """
        self.url = seedUrl

    def getWebData(self):
        """Get data from a web server.

        Args:
            - none

        Returns:
            - output - text with HTML code converted into lowercase
        """
        response = requests.get(self.url)

        print(response.status_code)
        print(response.headers)

        return response.text.lower()
