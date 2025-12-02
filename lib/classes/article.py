# Article class: connects an Author to a Magazine.
# Each article has 1 author, 1 magazine, and a title.

class Article:
    # Store ALL articles to help with relationships
    all = []

    def __init__(self, author, magazine, title):
        # Validate author
        from .author import Author
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance.")

        # Validate magazine
        from .magazine import Magazine
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance.")

        # Validate title
        if not isinstance(title, str):
            raise Exception("title must be a string.")
        if not (5 <= len(title) <= 50):
            raise Exception("title must be 5 to 50 characters.")

        # Assign values
        self._author = author
        self._magazine = magazine
        self._title = title  # title NEVER changes

        Article.all.append(self)

    
    @property
    def title(self):
        return self._title

    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance.")
        self._author = value

    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance.")
        self._magazine = value
