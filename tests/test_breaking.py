import unittest
from app.models import Breaking


class KeywordTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Keyword class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_breaking = Breaking('El cargador universal USB-C al fin tiene fecha: la Unión Europea da otro paso hacia su implantación.',
                                     'https://www.abcnews.com', 'https://www.xataka.com/accesorios/cargador-universal-usb-c-al-fin-tiene-fecha-union-europea-da-otro-paso-su-implantacion')

    def test_instance(self):
        '''
        Test case to test if the object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_breaking, Breaking))

    def test_initialization(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_breaking.title,
                         'El cargador universal USB-C al fin tiene fecha: la Unión Europea da otro paso hacia su implantación.')
        self.assertEqual(self.new_breaking.imageurl, 'https://www.abcnews.com')


if __name__ == '__main__':
    unittest.main()
