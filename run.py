from scrape.GoodReads import GoodReads

goodreads = GoodReads("https://www.goodreads.com/quotes")
#goodreads = GoodReads("https://www.goodreads.com/quotes/tag/love")
goodreadQuotes = goodreads.getQuotes()

for quote in goodreadQuotes:
    quote.prettyprint()

print(len(goodreadQuotes))
