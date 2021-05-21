from src import comb_testing
import profile


def main():
    # prompt for user input

    test_list = [["orientation_portrait", "orientation_landscape"],["power_on", "power_off"],["internet_connected", "internet_disconnected"],["battery_low", "battery_okay", "battery_high"]]

    large_list = comb_testing.generate_covering_array("2^4")

    suite = comb_testing.greedy_algorithm(test_list, 4)
    print(len(suite))
    print(suite)


if __name__ == '__main__':
    profile.run("main()")
