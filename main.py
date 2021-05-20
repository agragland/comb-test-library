from src import comb_testing


def main():
    # prompt for user input
    cover_input = input("Input as follows - \"#Levels^#Factors\" - put a space between each for multi-level covering:")

    new_list = comb_testing.generate_covering_array(cover_input)

    suite = comb_testing.greedy_algorithm(new_list, 2)

    print(len(suite))
    print(suite)
    comb_testing.test_suite_output(suite)


if __name__ == '__main__':
    main()
