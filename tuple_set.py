class TupleSet:

    def __init__(self, new_list, n):
        self.tuple_set = set()
        self.tuple_copy = set()
        self.covering_arr = new_list
        self.covered = 0
        self.total_tuples = 0
        self.strength = n

    def n_way_recursion(self, depth, t, f):
        if depth == self.strength:
            self.tuple_set.add(t)
        else:
            for fct in range(f, len(self.covering_arr)):
                for lvl in self.covering_arr[fct]:
                    nest_t = t + (lvl,)
                    self.n_way_recursion(depth + 1, nest_t, fct+1)

    def update_tuples(self):
        self.total_tuples = len(self.tuple_set)
        self.tuple_copy = self.tuple_set.copy()

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
