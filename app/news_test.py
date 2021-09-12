import unittest
from .models import news

Source = news.Source
Article = news.Article

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("Associated Press" "Associated Press","general","The AP delivers in-depth coverage on the international, politics, lifestyle, business, and entertainment news.","en")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article("https://thenextweb.com/news/what-mean-when-company-says-we-do-not-sell-your-data-syndication",'What does it actually mean when a company says, "We do not sell your data"?',"You’ve likely run into this claim from tech giants before: “We do not sell your personal data.”\r\n\r\nCompanies from Facebook to Google to Twitter repeat versions of this statement ...","2021-09-12T10:00:29Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()

