from src.comb_testing.tuple_set import TupleSet
from src.comb_testing.test_suite import TestSuite
import re


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


def test_suite_output(suite):
    file_out = open("aetg_output.txt", "w")

    file_out.write(str(len(suite)) + "\n\n")

    for candidate in suite:
        file_out.write(str(candidate) + "\n")

    file_out.close()


def greedy_algorithm(new_list, strength):
    tuples = TupleSet(new_list, strength)
    tuples.n_way_recursion(0, (), 0)
    tuples.update_tuples()

    # generate 100 test suites
    test_suites = []
    for i in range(100):
        suite = TestSuite(tuples)
        test_suites.append(suite.generate_suite())

    lowest_suite = test_suites[0]
    lowest = len(lowest_suite)

    for suite in test_suites:
        if len(suite) < lowest:
            lowest = len(suite)
            lowest_suite = suite

    return lowest_suite
