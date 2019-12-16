from scrape.BaseScraper import BaseScraper
from scrape.RequestsWrapper import RequestsWrapper
from bs4 import BeautifulSoup
from scrape.Quote import Quote

class GoodReads(BaseScraper):
    RequestsWrapper = None
    
    def __init__(self, url):
        self.RequestsWrapper = RequestsWrapper(url)

    def getQuotes(self):
        allQuotes = []
        soup = BeautifulSoup(self.RequestsWrapper.getURLBody(), features="html.parser")
        rawQuotes = soup.find_all("div", class_="quoteDetails")
        for quoteDiv in rawQuotes:
            quoteDetails = quoteDiv.find("div", class_="quoteText").get_text()
            author = quoteDiv.find("span", class_="authorOrTitle").get_text().lstrip("\\n").rstrip("\\n")
            author = author[4:author.find("\\n")].strip()
            quoteStart = quoteDetails.find("“")
            quoteEnd = quoteDetails.find("”")
            content = quoteDetails[quoteStart+1:quoteEnd]
            isCode = quoteDetails.find("//")
            if (isCode != -1):
                book = quoteDiv.find("a", class_="authorOrTitle").text.strip('\n').strip()
                author += " " + book
            newQuote = Quote(content, author, [])
            allQuotes.append(newQuote)
        return allQuotes
