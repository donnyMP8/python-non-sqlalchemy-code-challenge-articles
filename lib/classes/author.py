# Author class: represents a writer who can write many articles.

class Author:
    def __init__(self, name):
        # Name must be a string, longer than 0 chars.
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if len(name.strip()) == 0:
            raise Exception("Name cannot be empty.")

        # name should NEVER change after creation
        self._name = name

    @property
    def name(self):
        return self._name

    # Returns all Article instances written by this author.
    def articles(self):
        from .article import Article
        return [article for article in Article.all if article.author == self]

    # Returns a UNIQUE list of Magazine instances the author has written for.
    def magazines(self):
        mags = [article.magazine for article in self.articles()]
        # use set() to remove duplicates
        return list(set(mags))

    # Bonus: create a new article and connect it to this author.
    def add_article(self, magazine, title):
        from .article import Article
        return Article(self, magazine, title)

    # Bonus: list of UNIQUE magazine categories the author has written for.
    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list(set([mag.category for mag in mags]))
