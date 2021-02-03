import unittest


def has_palindrome_permutation(s):

    # Check if any permutation of the input is a palindrome
    # odd_chars = set()
    # for char in the_string:
    #     if char in odd_chars:
    #         odd_chars.remove(char)
    #     else:
    #         odd_chars.add(char)

    # return len(odd_chars) <=1

    value = 0
#Using value to maintain each letter's odd/even status

    for ch in s:
        ch_code = ord(ch) #represent each character with a bit using its ASCII number.
        value ^= (1 << ch_code)  #for each character you can flip the bit with xor
    #return value & (value - 1)  == 0  #a bit AND trick to determine if there are more than one set bit in the bit vector (also returns true for 0 set bits). In the end, if there is at most single 1 bit remaining, then it is a palindrome.
    return value == value & -value  #can quickly test this by checking if the least significant 1 bit (n & -n) is the same as itself.















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)