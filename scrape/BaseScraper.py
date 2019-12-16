from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, url):
        super().__init__(url)

    @abstractmethod
    def getQuotes(self):
        pass
