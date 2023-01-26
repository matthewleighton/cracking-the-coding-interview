import unittest
from problem1_3 import urlify

class TestProblem3(unittest.TestCase):
    
    def test_one_space(self):
        result = urlify('a b')
        self.assertEqual(result, 'a%20b')
    
    def test_two_spaces(self):
        result = urlify('a b c')
        self.assertEqual(result, 'a%20b%20c')

    def test_no_spaces(self):
        result = urlify('abc')
        self.assertEqual(result, 'abc')


if __name__ == '__main__':
	unittest.main()