class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name,str):
            raise TypeError("name must be of typestring")
        if len(name) == 0:
            raise ValueError("name must be longer than 0 characters")
        self.name = name
    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all() if article.author == self]
        
        
    
        

    def magazines(self):
        return list({article.magazine for article in self.articles()})
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass