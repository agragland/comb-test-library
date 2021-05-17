import random


class TestSuite:
    def __init__(self, tuple_dict):
        self.tuples = tuple_dict
        self.covering_arr = tuple_dict.get_covering_arr()
        self.suite = []
        self.factor_order = list(range(len(self.covering_arr)))

    def generate_suite(self):

        best_candidate = Candidate(len(self.covering_arr))

        while self.tuples.get_tuples_covered() < self.tuples.get_total_tuples():

            best_total = -1

            for i in range(50):

                curr_candidate = Candidate(len(self.covering_arr))

                random.shuffle(self.factor_order)
                potential_lvls = []
                running_total = 0
                best_count = -1
                curr_factor = 0

                # first factor
                for val in self.covering_arr[self.factor_order[curr_factor]]:
                    count = self.tuples.count_tuples_value(val, self.factor_order[curr_factor])
                    if count > best_count:
                        best_count = count
                        potential_lvls.clear()
                        potential_lvls.append(val)
                    elif count == best_count:
                        potential_lvls.append(val)

                curr_candidate.update(self.factor_order[curr_factor], random.choice(potential_lvls))
                curr_factor += 1

                # remaining factors
                while curr_factor < len(self.factor_order):
                    best_count = -1
                    potential_lvls.clear()

                    for val in self.covering_arr[self.factor_order[curr_factor]]:
                        curr_candidate.update(self.factor_order[curr_factor], val)
                        count = self.tuples.count_tuples_candidate(curr_candidate.ret_tuple(), self.factor_order[curr_factor])
                        if count > best_count:
                            best_count = count
                            potential_lvls.clear()
                            potential_lvls.append(val)
                        elif count == best_count:
                            potential_lvls.append(val)

                    curr_candidate.update(self.factor_order[curr_factor], random.choice(potential_lvls))
                    running_total += best_count
                    curr_factor += 1

                if running_total >= best_total:
                    best_total = running_total
                    best_candidate = curr_candidate

            self.suite.append(best_candidate)
            self.tuples.cover_tuples(best_candidate.ret_tuple())

        self.tuples.reset_tuples()
        return self.suite





class Candidate:
    def __init__(self, num_factors):
        self.num_factors = num_factors
        self.candidate = [-1] * num_factors

    def update(self, index, val):
        self.candidate[index] = val

    def reset(self):
        self.candidate = [-1] * self.num_factors

    def ret_tuple(self):
        return tuple(self.candidate)


class TupleDict:

    def __init__(self, new_list):
        self.tuple_dict = {}
        self.covering_arr = new_list
        self.covered = 0
        self.nums = [0] * 12

        # generate pairs
        curr_factor = 0
        for fct in self.covering_arr:
            for lvl in fct:
                for pair_fct in range(curr_factor + 1, len(self.covering_arr)):
                    for pair_lvl in self.covering_arr[pair_fct]:
                        self.tuple_dict.update({(lvl, pair_lvl): False})
            curr_factor += 1

    def count_tuples_value(self, val, index):
        count = 0
        for i in range(index):
            for lvl in self.covering_arr[i]:
                if self.tuple_dict.get((lvl, val)) is False:
                    count += 1

        for i in range(index + 1, len(self.covering_arr)):
            for lvl in self.covering_arr[i]:
                if self.tuple_dict.get((val, lvl)) is False:
                    count += 1

        return count

    def count_tuples_candidate(self, candidate, index):
        count = 0
        for i in range(index):
            if self.tuple_dict.get((candidate[i], candidate[index])) is False:
                count += 1
        for i in range(index + 1, len(candidate)):
            if self.tuple_dict.get((candidate[index], candidate[i])) is False:
                count += 1
        return count

    def cover_tuples(self, candidate):
        for i in range(len(candidate) - 1):
            for j in range(i + 1, len(candidate)):
                self.tuple_dict[(candidate[i], candidate[j])] = True
                self.covered += 1

    def reset_tuples(self):
        for i in self.tuple_dict:
            self.tuple_dict[i] = False
        self.covered = 0

    def get_total_tuples(self):
        return len(self.tuple_dict)

    def get_tuples_covered(self):
        return self.covered

    def get_covering_arr(self):
        return self.covering_arr
