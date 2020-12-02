import unittest
from models import article
Article=article.Article

class ArticleTest(unittest.TestCase):
    
    #Test the news article class
    
    def setUp(self):
        
        #Setup method that will run before every test
       
        self.new_article =Article('o','r','n','e','lla kak nka','www.ma.com/','www.ma.com/p.jpg','zik y')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()