import random


class TestSuite:
    def __init__(self, tuple_dict):
        self.tuples = tuple_dict
        self.covering_arr = tuple_dict.get_covering_arr()
        self.suite = []
        self.factor_order = list(range(len(self.covering_arr)))

    def generate_suite(self):

        best_candidate = [-1] * len(self.covering_arr)

        while self.tuples.get_tuples_covered() < self.tuples.get_total_tuples():

            best_total = -1

            for i in range(50):

                curr_candidate = [-1] * len(self.covering_arr)

                random.shuffle(self.factor_order)
                potential_lvls = []
                running_total = 0
                best_count = -1
                curr_factor = 0

                # first factor
                factor_index = self.factor_order[curr_factor]

                for val in self.covering_arr[factor_index]:
                    self.tuples.count_tuples_value(val, factor_index, 1, (val,), 0)
                    if (count := self.tuples.get_tuple_count()) > best_count:
                        best_count = count
                        potential_lvls.clear()
                        potential_lvls.append(val)
                    elif count == best_count:
                        potential_lvls.append(val)

                curr_candidate[factor_index] = random.choice(potential_lvls)
                curr_factor += 1

                # remaining factors
                while curr_factor < len(self.factor_order):
                    best_count = -1
                    potential_lvls.clear()
                    factor_index = self.factor_order[curr_factor]

                    for val in self.covering_arr[factor_index]:
                        curr_candidate[factor_index] = val
                        self.tuples.count_tuples_candidate(curr_candidate, 0, (), 0)
                        if (count := self.tuples.get_tuple_count()) > best_count:
                            best_count = count
                            potential_lvls.clear()
                            potential_lvls.append(val)
                        elif count == best_count:
                            potential_lvls.append(val)

                    curr_candidate[factor_index] = random.choice(potential_lvls)
                    running_total += best_count
                    curr_factor += 1

                if running_total >= best_total:
                    best_total = running_total
                    best_candidate = curr_candidate.copy()

            self.suite.append(best_candidate)
            self.tuples.cover_tuples(best_candidate, 0, (), 0)

        self.tuples.reset_tuples()
        return self.suite
