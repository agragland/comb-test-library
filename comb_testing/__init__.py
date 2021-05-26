# __init__.py

# Version of the combinatorial_tests package
__version__ = "0.0.1"

from comb_testing.tuple_set import TupleSet
from comb_testing.test_suite import TestSuite
import re


# function to generate a covering array based on input
# input follows formatting "Input as follows - \"#Levels^#Factors\" -
# put a space bgenerate_covering_arrayetween each for multi-level covering:"
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


def check_valid_input(new_list):
    uniq = set()
    for fct in new_list:
        if len(fct) == 0:
            return False
        else:
            for lvl in fct:
                if lvl in uniq:
                    return False
                else:
                    uniq.add(lvl)
    return True


# function to run the greedy version of the combinatorial testing algorithm
# new_list is a 2D list where the outer layer represents the factors and the inner layer represents the levels
# strength represents the n of n-way coverage
def greedy_algorithm(new_list, strength):
    if strength > len(new_list):
        print("Error: Coverage strength greater than factor count")
        return []
    if not check_valid_input(new_list):
        print("Error: Input list is invalid")

    tuples = TupleSet(new_list, strength)

    suite = TestSuite(tuples)
    test = suite.generate_greedy_suite()

    return test
