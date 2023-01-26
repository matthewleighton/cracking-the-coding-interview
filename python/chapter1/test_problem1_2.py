import unittest
from problem1_2 import is_permutation

class TestProblem2(unittest.TestCase):
    
    def test_correctly_returns_true(self):
        string1, string2 = 'abc', 'bca'
        result = is_permutation(string1, string2)
        self.assertTrue(result)

    def test_correctly_returns_false(self):
        string1, string2 = 'abc', 'abcd'
        result = is_permutation(string1, string2)
        self.assertFalse(result)

        string1, string2 = 'qwe', 'qyw'
        result = is_permutation(string1, string2)
        self.assertFalse(result)


if __name__ == '__main__':
	unittest.main()