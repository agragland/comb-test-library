# __init__.py

# Version of the combinatorial_tests package
__version__ = "0.0.4"

from comb_testing.tuple_set import TupleSet
from comb_testing.test_suite import TestSuite
from comb_testing.biased_algorithm import generate_biased_suite
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
def greedy_algorithm(new_list, strength, flag):
    if strength > len(new_list):
        print("Error: Coverage strength greater than factor count")
        return []
    if not check_valid_input(new_list):
        print("Error: Input list is invalid")
        return

    tuples = TupleSet(new_list, strength)
    tuples.n_way_recursion(0, (), 0)
    tuples.update_tuples()

    # generate a test suite
    suite = TestSuite(tuples)

    if flag == 1:
        return suite.generate_greedy_suite_size()
    elif flag == 2:
        tuples.generate_combos()
        return suite.generate_greedy_suite_speed()


# function to run the biased version of the combinatorial testing algorithm
# new_list and benefit_list 2D lists of equal size and depth which map a "benefit" value to each value in the main list
# exclusions is a list which contains pairs to be excluded from final test cases
def biased_algorithm(new_list, benefit_list, exclusions):
    if not check_valid_input(new_list):
        print("Error: Input list is invalid")
        return

    return generate_biased_suite(new_list, benefit_list, exclusions)
