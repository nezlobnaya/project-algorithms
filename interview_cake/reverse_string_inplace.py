import unittest


def reverse(list_of_chars):

    # Reverse the input list of chars in place
    left_ptr = 0
    right_ptr = len(list_of_chars) -1
    
    while left_ptr < right_ptr:
        list_of_chars[left_ptr], list_of_chars[right_ptr] = list_of_chars[right_ptr],list_of_chars[left_ptr]
        
        left_ptr +=1
        right_ptr -=1

    # return list_of_chars[::-1]


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)


unittest.main(verbosity=2)