# Combinatorial Testing Package
This package allows a user to input a list of **n** factors and **k** levels with a coverage strength value **t** to
create an optimal suite of tests that can be run.

## Primary Function

To import the package once installed, use:

`import comb_testing`

Once imported, the primary function to use is called using:

`comb_testing.greedy_algorithm(<list>, <strength>)`

Where `<list>` is the **N** x **k** list of factors and levels and `<strength>` is the **t** value


## Covering Array Generation

If there is no predetermined list, this package features a function to generate a covering array based on a regex string

The function can be called using:
`comb_testing.generate_covering_array("<regex>")`

The value of `<regex>` will be a string with the following format: `"<N>^<k> <N>^<k> ..."`

An example of this function to generate a covering array with 4 factors and 3 levels would be:

`covering_arr = comb_testing.generate_covering_array("3^4")`

In this example, the result is stored in `covering_arr` and can be iterated over like any other list