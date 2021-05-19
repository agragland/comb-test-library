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


def generate_tuples(new_list, avoid):
    ret_list = []

    for factor in new_list:
        if new_list.index(factor) != avoid:
            ret_list.extend(factor)

    return ret_list


def main():
    test_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

    suite = []
    covered_tuples = []
    while len(covered_tuples) < 54:

        candidate_row = []
        tuples = []
        for factor in test_list:
            candidate_set = set()
            for value in factor:
                tuples = generate_tuples(test_list, test_list.index(factor))
                for t in tuples:
                    if t < value:
                        selected_tuple = (t, value)
                        if selected_tuple not in covered_tuples:
                            candidate_set.add(value)
                            break
                    elif t > value:
                        selected_tuple = (value, t)
                        if selected_tuple not in covered_tuples:
                            candidate_set.add(value)
                            break
            if len(candidate_set) > 0:
                selected_value = random.choice(list(candidate_set))
            for t in tuples:
                if t < selected_value:
                    new_tuple = (t, selected_value)
                    if new_tuple not in covered_tuples and t in candidate_row:
                        covered_tuples.append(new_tuple)
                elif selected_value < t:
                    new_tuple = (selected_value, t)
                    if new_tuple not in covered_tuples and t in candidate_row:
                        covered_tuples.append(new_tuple)
            candidate_row.append(selected_value)
        suite.append(candidate_row)


    # input list of of t factors and k levels L_tk = (N; n, t, k)
    # input event combination strength, n
    # output n-way covering array
    for row in suite:
        print(row)


if __name__ == '__main__':
    main()
