class TupleSet:

    def __init__(self, new_list, n):
        self.tuple_set = set()
        self.tuple_copy = set()
        self.covering_arr = new_list
        self.covered = 0
        self.total_tuples = 0
        self.strength = n
        self.tuple_count = 0

    def n_way_recursion(self, depth, t, f):
        if depth == self.strength:
            self.tuple_set.add(t)
        else:
            for fct in range(f, len(self.covering_arr)):
                for lvl in self.covering_arr[fct]:
                    nest_t = t + (lvl,)
                    self.n_way_recursion(depth + 1, nest_t, fct + 1)

    def update_tuples(self):
        self.total_tuples = len(self.tuple_set)
        self.tuple_copy = self.tuple_set.copy()

    def count_tuples_value(self, val, index, depth, t, f):
        if depth == self.strength:
            if t in self.tuple_set:
                self.tuple_count += 1
        else:
            for fct in range(f, len(self.covering_arr)):
                if val in self.covering_arr[fct]:
                    continue
                else:
                    if fct < index:
                        for lvl in self.covering_arr[fct]:
                            nest_t = (lvl,) + t
                            self.count_tuples_value(val, index, depth + 1, nest_t, fct + 1)
                    elif fct > index:
                        for lvl in self.covering_arr[fct]:
                            nest_t = t + (lvl,)
                            self.count_tuples_value(val, index, depth + 1, nest_t, fct + 1)

    def count_tuples_candidate(self, candidate, depth, t, f):
        if depth == self.strength:
            if t in self.tuple_set:
                self.tuple_count += 1
        else:
            for i in range(f, len(candidate)):
                nest_t = t + (candidate[i],)
                self.count_tuples_candidate(candidate, depth + 1, nest_t, i + 1)

    def cover_tuples(self, candidate, depth, t, f):
        if depth == self.strength:
            if t in self.tuple_set:
                self.tuple_set.discard(t)
                self.covered += 1
        else:
            for i in range(f, len(candidate)):
                nest_t = t + (candidate[i],)
                self.cover_tuples(candidate, depth + 1, nest_t, i + 1)

    def reset_tuples(self):
        self.tuple_set = self.tuple_copy.copy()
        self.covered = 0

    def get_total_tuples(self):
        return self.total_tuples

    def get_tuples_covered(self):
        return self.covered

    def get_tuple_count(self):
        ret = self.tuple_count
        self.tuple_count = 0
        return ret

    def get_covering_arr(self):
        return self.covering_arr
