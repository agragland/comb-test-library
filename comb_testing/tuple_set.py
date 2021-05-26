# TupleSet class within comb_testing package
# Copyright Andrew Ragland 2021
import itertools


class TupleSet:

    def __init__(self, new_list, n):
        self.tuple_set = set()
        self.tuple_copy = set()
        self.covering_arr = new_list
        self.factor_count = len(self.covering_arr)
        self.strength = n

        self.combos = list(itertools.combinations([lvl for fct in self.covering_arr for lvl in fct], len(self.covering_arr)))

    # counter the number of tuples a specified candidate can cover
    def count_tuples_candidate(self, candidate):
        count = 0
        tuples = itertools.combinations(candidate, self.strength)
        for t in tuples:
            if t in self.tuple_set:
                count += 1
        return count

    # cover the tuples as found within a specified candidate
    def cover_tuples(self, candidate):
        tuples = itertools.combinations(candidate, self.strength)
        for t in tuples:
            if t in self.tuple_set:
                self.tuple_set.discard(t)

    def is_empty(self):
        return False if self.tuple_set else True

    def get_covering_arr(self):
        return self.covering_arr
