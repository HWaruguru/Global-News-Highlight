class Source:
    '''
    Source class to define Source Objects
    '''

    def __init__(self, id, name, category, description, language):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.language  = language


class Article:
    '''
    Article class to define Article objects
    '''
    def __init__(self, url, urlToImage, title, description, publishedAt):
        self.url = url
        self.urlToImage = urlToImage
        self.title = title
        self.description = description
        self.publishedAt = publishedAt



