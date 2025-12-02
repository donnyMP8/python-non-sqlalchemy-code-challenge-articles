# Magazine class: has many articles, and many authors.

class Magazine:
    # Keep track of ALL magazine instances for top_publisher()
    all = []

    def __init__(self, name, category):
        # Validate name
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        if not (2 <= len(name) <= 16):
            raise Exception("Name must be 2 to 16 characters.")

        # Validate category
        if not isinstance(category, str):
            raise Exception("Category must be a string.")
        if len(category.strip()) == 0:
            raise Exception("Category cannot be empty.")

        self._name = name
        self._category = category

        Magazine.all.append(self)

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string.")
        if not (2 <= len(value) <= 16):
            raise Exception("Name must be 2 to 16 characters.")
        self._name = value

    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string.")
        if len(value.strip()) == 0:
            raise Exception("Category cannot be empty.")
        self._category = value

    # Return all articles that belong to this magazine.
    def articles(self):
        from .article import Article
        return [article for article in Article.all if article.magazine == self]

    # Unique list of authors who wrote for this magazine.
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
    """test section to exercices a lil bit """

    #: list of article title strings. None if no articles.
    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    #: authors with more than 2 articles in this magazine.
    def contributing_authors(self):
        authors = self.contributors()
        result = []

        for author in authors:
            count = len([a for a in self.articles() if a.author == author])
            if count > 2:
                result.append(author)

        return result if result else None

    # returns Magazine with most published articles
    @classmethod
    def top_publisher(cls):
        from .article import Article
        if not Article.all:
            return None

        return max(cls.all, key=lambda mag: len(mag.articles()))
