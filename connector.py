import requests

class Connector:
    url = ''

    def __init__(self, seedUrl):
        self.url = seedUrl

    def getWebData(self):
        response = requests.get(self.url)
        print(response.status_code)
        print(response.headers)
        return response.text.lower()
