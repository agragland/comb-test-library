from tuple_set import TupleSet
from test_suite import TestSuite
import time, re, random


def generate_covering_array(re_input):
    match_list = re.findall("(\\d+)\\^(\\d+)", re_input)

    cover_arr = []
    lvl_offset = 0
    for match in match_list:
        levels = int(match[0])
        factors = int(match[1])

        for i in range(factors):
            row = []
            for j in range(levels):
                row.append(j + lvl_offset)

            lvl_offset += levels
            cover_arr.append(row)
    return cover_arr


def generate_tuples(new_list, strength):
    n_strength = strength-1
    out_tuples = []
    for fct in new_list:
        for lvl in fct:
            mid_tuple = (lvl,)
            for s in range(n_strength):
                for tuple_fct in range(new_list.index(fct) + n_strength, len(new_list)):
                    for tuple_lvl in new_list[tuple_fct]:
                        out_tuple = mid_tuple + (tuple_lvl,)
                        for i in range(n_strength-s):
                            out_tuples.append(out_tuple)
    return out_tuples

def generate_tup(new_list, val):
    tuples = []
    for fct in new_list:
        if val in fct:
            continue
        for lvl in fct:
            if val < lvl:
                tuples.append((val,lvl))
            elif val > lvl:
                tuples.append((lvl, val))
    return tuples


def main():
    test_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]  # t = 4 factors, k = 3 levels, n = 2

    suite = []  # L_all
    tuples = generate_tuples(test_list, 2)
    total_covered = 0
    total_tuples = len(tuples)
    covered_tuples = []

    while total_covered < total_tuples:
        candidate_row = []

        for fct in test_list:
            candidate_set = []
            for val in fct:
                tps = generate_tup(test_list, val)
                for t in tps:
                    if t in tuples:
                        candidate_set.append(val)
                        break
                    else:
                        candidate_set.append(tuples[0][0])

            selected_val = random.choice(candidate_set)
            candidate_row.append(selected_val)

        for i in range(len(candidate_row) - 1):
            for j in range(i + 1, len(candidate_row)):
                if (candidate_row[i], candidate_row[j]) in tuples:
                    tuples.remove((candidate_row[i], candidate_row[j]))
                    total_covered += 1

        suite.append(candidate_row)






    # while True:
    #
    #     candidate_row = []
    #     tuples = []
    #     for factor in test_list:
    #         candidate_set = set()
    #         for value in factor:
    #             tuples = generate_tuples(test_list, test_list.index(factor))
    #             for t in tuples:
    #                 if t < value:
    #                     selected_tuple = (t, value)
    #                     if selected_tuple not in covered_tuples:
    #                         candidate_set.add(value)
    #                         break
    #                 elif t > value:
    #                     selected_tuple = (value, t)
    #                     if selected_tuple not in covered_tuples:
    #                         candidate_set.add(value)
    #                         break
    #         if len(candidate_set) > 0:
    #             selected_value = random.choice(list(candidate_set))
    #         for t in tuples:
    #             if t < selected_value:
    #                 new_tuple = (t, selected_value)
    #                 if new_tuple not in covered_tuples and t in candidate_row:
    #                     covered_tuples.append(new_tuple)
    #             elif selected_value < t:
    #                 new_tuple = (selected_value, t)
    #                 if new_tuple not in covered_tuples and t in candidate_row:
    #                     covered_tuples.append(new_tuple)
    #         candidate_row.append(selected_value)
    #     suite.append(candidate_row)

    # input list of of t factors and k levels L_tk = (N; n, t, k)
    # input event combination strength, n
    # output n-way covering array
    for row in suite:
        print(row)


if __name__ == '__main__':
    main()
