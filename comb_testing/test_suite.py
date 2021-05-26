# TestSuite class within comb_testing package
# Copyright Andrew Ragland 2021

import random, itertools


class TestSuite:
    def __init__(self, tuple_dict):
        self.tuples = tuple_dict
        self.covering_arr = tuple_dict.get_covering_arr()
        self.factor_count = len(self.covering_arr)
        self.suite = []
        self.factor_order = list(range(self.factor_count))

    def check_valid_candidate(self, candidate):
        for fct_ind in range(self.factor_count):
            if not candidate[fct_ind] in self.covering_arr[fct_ind]:
                return False
        return True

    # generate a test suite and return it using the greedy method
    def generate_greedy_suite(self):

        while not self.tuples.is_empty():
            counts = []
            for row in self.tuples.combos:
                counts.append(self.tuples.count_tuples_candidate(row))
            test = list(itertools.zip_longest(self.tuples.combos, counts))
            test = sorted(test, key=lambda x: x[1], reverse=True)

            for row in test:
                if self.check_valid_candidate(row[0]):
                    self.tuples.cover_tuples(row[0])
                    self.suite.append(row[0])
                    break

        return self.suite
