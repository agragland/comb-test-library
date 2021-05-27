# TestSuite class within comb_testing package
# Copyright Andrew Ragland 2021

import itertools
import random


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
    def generate_greedy_suite_size(self):

        while not self.tuples.is_empty():

            curr_candidate = [-1] * self.factor_count

            random.shuffle(self.factor_order)
            potential_lvls = []
            best_count = -1
            curr_factor = 0

            # first factor
            factor_index = self.factor_order[curr_factor]

            for val in self.covering_arr[factor_index]:
                self.tuples.count_tuples_value(val, factor_index, 1, (val,), 0)
                if (count := self.tuples.get_tuple_count()) > best_count:
                    best_count = count
                    potential_lvls[:] = [val]
                elif count == best_count:
                    potential_lvls.append(val)

            curr_candidate[factor_index] = random.choice(potential_lvls)
            curr_factor += 1

            # remaining factors
            while curr_factor < self.factor_count:
                best_count = -1
                potential_lvls[:] = []
                factor_index = self.factor_order[curr_factor]

                for val in self.covering_arr[factor_index]:
                    curr_candidate[factor_index] = val
                    self.tuples.count_tuples_candidate(curr_candidate)
                    if (count := self.tuples.get_tuple_count()) > best_count:
                        best_count = count
                        potential_lvls[:] = [val]
                    elif count == best_count:
                        potential_lvls.append(val)

                curr_candidate[factor_index] = random.choice(potential_lvls)
                curr_factor += 1

            self.suite.append(curr_candidate)
            self.tuples.cover_tuples(curr_candidate)

        self.tuples.reset_tuples()
        return self.suite

    # generate a test suite by first generating all possible candidate rows and add to suite based on maximum coverage
    def generate_greedy_suite_speed(self):
        while not self.tuples.is_empty():
            counts = []
            for row in self.tuples.combos:
                self.tuples.count_tuples_candidate(row)
                counts.append(self.tuples.get_tuple_count())
            test = list(itertools.zip_longest(self.tuples.combos, counts))
            test = sorted(test, key=lambda x: x[1], reverse=True)

            for row in test:
                if self.check_valid_candidate(row[0]):
                    self.tuples.cover_tuples(row[0])
                    self.suite.append(row[0])
                    break

        return self.suite
