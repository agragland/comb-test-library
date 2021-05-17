from classes import TestSuite, TupleDict


def generate_covering_array(num_levels, num_factors):
    lvl_offset = 0
    cover_arr = []
    for i in range(num_factors):
        row = []
        for j in range(num_levels):
            row.append(lvl_offset)
            lvl_offset += 1
        cover_arr.append(row)

    return cover_arr


def test_suite_output(suite):
    file_out = open("aetg_output.txt", "w")

    file_out.write(str(len(suite))+"\n\n")

    for candidate in suite:
        file_out.write(str(candidate.ret_tuple())+"\n")

    file_out.close()


def main():
    new_list = generate_covering_array(3, 4)
    tuples = TupleDict(new_list)

    # generate 100 test suites
    test_suites = []
    for i in range(100):
        suite = TestSuite(tuples)
        print(str(i) + " %")
        test_suites.append(suite.generate_suite())

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
        suite_sum / 100) + "\n")

    test_suite_output(lowest_suite)


if __name__ == '__main__':
    main()
