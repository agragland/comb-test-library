from tuple_set import TupleSet
from test_suite import TestSuite
import time, re


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


def main():
    # prompt for user input
    cover_input = input("Input as follows - \"#Levels^#Factors\" - put a space between each for multi-level covering:")

    new_list = generate_covering_array(cover_input)
    tuples = TupleSet(new_list, 3)
    tuples.n_way_recursion(0, (), 0)
    tuples.update_tuples()

    # generate 100 test suites
    start_time = time.time()
    test_suites = []
    for i in range(100):
        suite = TestSuite(tuples)
        print(str(i) + " %")
        test_suites.append(suite.generate_suite())
    end_time = time.time()

    # run statistics
    lowest_suite = test_suites[0]
    lowest = len(lowest_suite)
    highest = 0

    suite_sum = 0
    for suite in test_suites:
        if len(suite) > highest:
            highest = len(suite)
        if len(suite) < lowest:
            lowest = len(suite)
            lowest_suite = suite
        suite_sum += len(suite)

    print("Results:\n"
          "Lowest AETG:" + str(lowest) + "\n"
                                         "Highest AETG: " + str(highest) + "\n"
                                                                           "Average AETG: " + str(
        suite_sum / 100) + "\n"
                           "Average Execution Time: " + "{:.6f}".format((end_time - start_time) / 100) + "\n")

    test_suite_output(lowest_suite)


if __name__ == '__main__':
    main()
