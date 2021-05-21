from unittest import TestCase
from tuple_set import TupleSet


class TestTupleSet(TestCase):
    def test_n_way_recursion(self):
        test_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
        tuples = TupleSet(test_list, 2)
        tuples.n_way_recursion(0, (), 0)
        tuples.update_tuples()

        self.assertEqual(54, tuples.get_total_tuples())

    def test_count_tuples_value(self):
        test_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
        tuples = TupleSet(test_list, 2)
        tuples.n_way_recursion(0, (), 0)
        tuples.update_tuples()

        tuples.count_tuples_value(3, 1, 1, (3,), 0)

        self.assertEqual(9, tuples.get_tuple_count())
