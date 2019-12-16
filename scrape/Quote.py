class Quote():

    def __init__(self, content, author, tags):
        self.content = content
        self.author = author 
        self.tags = tags

    def prettyprint(self):
        print("Quote is " + self.content)
        print("Author is " + self.author)
        print("Tags are " + ",".join(self.tags))
