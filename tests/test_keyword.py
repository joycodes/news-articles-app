import unittest
from app.models import Keyword


class KeywordTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Keyword class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_keyword = Keyword('Jeff Grubb', 'Are Square JRPGs endangered on Switch? | Last of the Nintendogs',
                                    'https://abcnews.com', '2022-05-04T01:03:30Z', 'https://venturebeat.com/2022/05/03/are-square-jrpgs-endangered-on-switch-last-of-the-nintendogs/')

    def test_instance(self):
        '''
        Test case to test if the object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_keyword, Keyword))

    def test_initialization(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_keyword.author, 'Jeff Grubb')
        self.assertEqual(self.new_keyword.imageurl, 'https://abcnews.com')


if __name__ == '__main__':
    unittest.main()
