import unittest
from app.models import Articles


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Jeff Grubb', 'Are Square JRPGs endangered on Switch? | Last of the Nintendogs',
                                    'https://abcnews.com', '2022-05-04T01:03:30Z', 'https://venturebeat.com/2022/05/03/are-square-jrpgs-endangered-on-switch-last-of-the-nintendogs/')

    def test_instance(self):
        '''
        Test case to test if the object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_initialization(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_article.author, 'Jeff Grubb')
        self.assertEqual(self.new_article.imageurl, 'https://abcnews.com')


if __name__ == '__main__':
    unittest.main()
