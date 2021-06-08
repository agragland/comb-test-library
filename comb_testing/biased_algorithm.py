# Biased Covering Array Algorithm - Andrew Ragland - 2021

import itertools
import random


# calculate a candidate's benefit value
def calc_candidate_benefit(tuples, candidate):
    can_benefit = 0
    tuple_count = 0
    pairs = list(itertools.combinations(candidate, 2))
    for pair in pairs:
        for tup in list(tuples.items()):
            if tup[0] == pair:
                can_benefit += tup[1]
                tuple_count += 1

    return can_benefit, tuple_count


# build a candidate out of a list of pairs
def build_candidate(cvr, pairs):
    candidate = [-1] * len(cvr)

    for pair in pairs:
        for fct in cvr:
            if pair[0] in fct:
                candidate[cvr.index(fct)] = pair[0]
            elif pair[1] in fct:
                candidate[cvr.index(fct)] = pair[1]

    return candidate


# perform pair generation using the recursive method
def two_way_recursion(depth, t, b, f, tuples, cvr, bft):
    if depth == 2:
        tuples.update({t: b})
    else:
        for fct in range(f, len(cvr)):
            for lvl in cvr[fct]:
                nest_t = t + (lvl,)
                nest_b = round(b * bft[fct][cvr[fct].index(lvl)], 2)
                two_way_recursion(depth + 1, nest_t, nest_b, fct + 1, tuples, cvr, bft)


def generate_biased_suite(covering_array, benefit_array, exclusion_array):
    cover_arr = covering_array
    benefit_arr = benefit_array
    exclusions = exclusion_array

    tuples = dict()

    test_suite = []

    two_way_recursion(0, (), 1, 0, tuples, cover_arr, benefit_arr)

    # exclusions - remove excluded pairs from the list of tuples
    if exclusions:
        for e in exclusions:
            tuples.pop(e)

    tuples = dict(sorted(tuples.items(), key=lambda item: item[1], reverse=True))

    while tuples:

        # store pairs where their benefit values are both maximum and equal
        eq_benefit_list = []
        eq_benefit_val = list(tuples.items())[0][1]

        factor_order = list(range(len(cover_arr)))
        random.shuffle(factor_order)

        for t in list(tuples.items()):
            if t[1] < eq_benefit_val:
                break
            else:
                eq_benefit_list.append(t[0])

        # random check
        init_tuple = random.choice(eq_benefit_list)

        init_can = build_candidate(cover_arr, [init_tuple])
        best_can = []
        for f in factor_order:
            max_benefit = 0
            max_count = 0
            if init_can[f] == -1:
                for val in cover_arr[f]:
                    init_can[f] = val
                    benefit, count = calc_candidate_benefit(tuples, init_can)
                    if benefit > max_benefit or count > max_count:
                        best_can = init_can.copy()
                        max_benefit = benefit
                        max_count = count

        # perform exclusions
        pairs = list(itertools.combinations(best_can, 2))

        final_can = []
        for p in pairs:
            if p in exclusions:
                # start exclusion process, determine pair indicies
                exc_benefit = 0
                exc_count = 0
                indices = [-1] * 2
                for i in range(len(cover_arr)):
                    if p[0] in cover_arr[i]:
                        indices[0] = i
                    elif p[1] in cover_arr[i]:
                        indices[1] = i

                for ind in indices:
                    exc_can = best_can.copy()
                    for val in cover_arr[ind]:
                        if val not in p:
                            exc_can[ind] = val
                            benefit, count = calc_candidate_benefit(tuples, exc_can)
                            if benefit > exc_benefit or count > exc_count:
                                final_can = exc_can.copy()
                                exc_benefit = benefit
                                exc_count = count
            else:
                final_can = best_can.copy()

        #
        final_pairs = list(itertools.combinations(final_can, 2))
        for p in final_pairs:
            for t in list(tuples.items()):
                if t[0] == p:
                    tuples.pop(t[0])
                    break
        if final_can:
            test_suite.append(final_can)

    return test_suite
