class TupleSet:

    def __init__(self, new_list):
        self.tuple_set = set()
        self.covering_arr = new_list
        self.covered = 0

        # generate pairs
        curr_factor = 0
        for fct in self.covering_arr:
            for lvl in fct:
                for to_pair_fct in range(curr_factor + 1, len(self.covering_arr)):
                    for to_pair_lvl in self.covering_arr[to_pair_fct]:
                        self.tuple_set.add((lvl, to_pair_lvl))
            curr_factor += 1

        self.tuple_copy = self.tuple_set.copy()
        self.total_tuples = len(self.tuple_set)

    def count_tuples_value(self, val, index):
        count = 0
        for i in range(index):
            for lvl in self.covering_arr[i]:
                if (lvl, val) in self.tuple_set:
                    count += 1

        for i in range(index + 1, len(self.covering_arr)):
            for lvl in self.covering_arr[i]:
                if (val, lvl) in self.tuple_set:
                    count += 1

        return count

    def count_tuples_candidate(self, candidate, index):
        count = 0
        for i in range(index):
            if (candidate[i], candidate[index]) in self.tuple_set:
                count += 1
        for i in range(index + 1, len(candidate)):
            if (candidate[index], candidate[i]) in self.tuple_set:
                count += 1
        return count

    def cover_tuples(self, candidate):
        for i in range(len(candidate) - 1):
            for j in range(i + 1, len(candidate)):
                if (candidate[i], candidate[j]) in self.tuple_set:
                    self.tuple_set.discard((candidate[i], candidate[j]))
                    self.covered += 1

    def reset_tuples(self):
        self.tuple_set = self.tuple_copy.copy()
        self.covered = 0

    def get_total_tuples(self):
        return self.total_tuples

    def get_tuples_covered(self):
        return self.covered

    def get_covering_arr(self):
        return self.covering_arr
