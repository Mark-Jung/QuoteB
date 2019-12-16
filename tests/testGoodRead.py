import unittest 
from unittest.mock import MagicMock
from scrape.GoodReads import GoodReads
from scrape.RequestsWrapper import RequestsWrapper

class GoodreadTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_goodreads_popular(self):
        url = "https://www.goodreads.com/quotes"
        path = "goodreadsPopular.html"
        firstQuote = "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best."
        firstQuoteAuthor = "Marilyn Monroe"
        lastQuote = "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover."
        lastQuoteAuthor = "H. Jackson Brown Jr., P.S. I Love You"
        goodreads = GoodReads(url)
        testWrapper = RequestsWrapper(url)
        with open(path, "r") as testFile:
            testHTML = str(testFile.readlines())
            testWrapper.getURLBody = MagicMock(return_value=testHTML)
            goodreads.RequestsWrapper = testWrapper
            goodreadQuotes = goodreads.getQuotes()
            self.assertTrue(30 == len(goodreadQuotes))
            self.assertEqual(firstQuote, goodreadQuotes[0].content)
            self.assertEqual(firstQuoteAuthor, goodreadQuotes[0].author)
            self.assertEqual(lastQuote, goodreadQuotes[-1].content)
            self.assertEqual(lastQuoteAuthor, goodreadQuotes[-1].author)
        pass
