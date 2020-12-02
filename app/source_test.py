import unittest
from models import source_news
News_Source=source_news.News_Source

class NewsSourceTest(unittest.TestCase):
    
    #Test  news source class
    
    def setUp(self):
        
        #set up method that will run before every test
        
        self.new_news = News_Source('n','k','www.ed.com',"l")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News_Source))

if __name__ == '__main__':
    unittest.main()