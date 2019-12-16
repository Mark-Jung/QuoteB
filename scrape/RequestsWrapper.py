import requests

class RequestsWrapper():
    def __init__(self, url):
        self.url = url

    def getURLBody(self):
        page = requests.get(self.url)
        return page.text
