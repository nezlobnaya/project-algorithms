import unittest


def merge_lists(my_list, alices_list):

    size = len(my_list) + len(alices_list)
    merged_list = [None] * size

    cur_ptr_mine = cur_ptr_alices = cur_ptr_merged = 0

    while cur_ptr_merged < size:
        is_mine_out = cur_ptr_mine >= len(my_list)
        is_alices_out = cur_ptr_alices >=len(alices_list)

        if (not is_mine_out and (is_alices_out or my_list[cur_ptr_mine] < alices_list[cur_ptr_alices])):
            merged_list[cur_ptr_merged] = my_list[cur_ptr_mine]
            cur_ptr_mine+=1
        else:
            merged_list[cur_ptr_merged] = alices_list[cur_ptr_alices]
            cur_ptr_alices+=1
        cur_ptr_merged+=1
    return merged_list


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)