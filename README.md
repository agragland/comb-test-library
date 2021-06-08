# Combinatorial Testing Package
This package allows a user to input a list of **n** factors and **k** levels with a coverage strength value **t** to
create an optimal suite of tests that can be run.

## Test Suite Generation

To import the package once installed, use:

`import comb_testing`

This package contains two types of algorithms designed to generate test suites. One uses a greedy method, while the other uses a weighted method.

### Greedy Algorithm
Once imported, the greedy algorithm function is called using:

`comb_testing.greedy_algorithm(<list>, <strength>, <flag>)`

Where `<list>` is the **N** x **k** list of factors and levels and `<strength>` is the **t** value

The `<flag>` value allows the user to select between two different algorithms for suite generation. 

The first, where `flag == 1` is an algorithm which is optimized for a larger covering array (one that exceeds more than 5 levels and/or 5 factors). 

The second, where `flag == 2` is an algorithm optimized for speed but is only fast with a smaller sized covering array.

The first algorithm is designed to be more traditionally greedy, but due to usage of random generation, final test suites can vary in size.

The second algorithm takes a more "back-to-front" approach by first generating all possible candidate rows and generating a suite based on 
how many tuples the top-most row can generate over time. 

### Biased Algorithm
A secondary algorithm which will generate a test suite through usage of a "benefit list" is available as well and can be called as

`comb_testing.biased_algorithm(<main_list>, <benefit_list>, <exclusions>)`

One note about this algorithm is that it can only support pairwise (2-way) coverage.

The structure `<main_list>` is similar to that of `<list>` as described above. It is an **N** x **k** list of factors and levels.

The `<benefit_list>` structure is also **N** x **k** size, but instead of unique values, the values are replaced with weights
or "benefit" values associated with the corresponding element in the `<main_list>`.

NOTE: If user intends to use `<benefit_list>` with covering array generation as dicussed below, a matching array with benefit values must be coded in place. 
Creating a function which will do this process automatically with a range of benefit values will be added in the future

Finally, `<exclusions>` allows the user to enter a list of pairwise tuples to exclude from the final test suite. For example, if a 
user wants to exclude the pair (2, 4) from the final suite, then the `<exclusions>` list would be `[(2,4)]` and so on for more than one pair.

## Covering Array Generation

If there is no predetermined list, this package features a function to generate a covering array based on a regex string

The function can be called using:
`comb_testing.generate_covering_array("<regex>")`

The value of `<regex>` will be a string with the following format: `"<N>^<k> <N>^<k> ..."`

An example of this function to generate a covering array with 4 factors and 3 levels would be:

`covering_arr = comb_testing.generate_covering_array("3^4")`

In this example, the result is stored in `covering_arr` and can be iterated over like any other list