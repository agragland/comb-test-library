from src.comb_testing.tuple_set import TupleSet
from src.comb_testing.test_suite import TestSuite
import re


# function to generate a covering array based on input
# input follows formatting "Input as follows - \"#Levels^#Factors\" -
# put a space between each for multi-level covering:"
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


# function to take a test suite and output contents to file
def test_suite_output(suite):
    file_out = open("aetg_output.txt", "w")

    file_out.write(str(len(suite)) + "\n\n")

    for candidate in suite:
        file_out.write(str(candidate) + "\n")

    file_out.close()


# function to run the greedy version of the combinatorial testing algorithm
# new_list is a 2D list where the outer layer represents the factors and the inner layer represents the levels
# strength represents the n of n-way coverage
def greedy_algorithm(new_list, strength):
    if strength > len(new_list):
        print("Error: Coverage strength greater than factor count")
        return []

    tuples = TupleSet(new_list, strength)
    tuples.n_way_recursion(0, (), 0)
    tuples.update_tuples()

    # generate 100 test suites
    test_suites = []

    def get_suite():
        suite = TestSuite(tuples)
        return suite.generate_greedy_suite()

    test_suites = [get_suite() for suite in range(100)]

    lowest_suite = test_suites[0]
    lowest = len(lowest_suite)

    for suite in test_suites:
        if len(suite) < lowest:
            lowest = len(suite)
            lowest_suite = suite

    return lowest_suite
