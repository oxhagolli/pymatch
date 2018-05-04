"""
Author: Orens Xhagolli
"""

from algorithms import gale_shapley


def realistic_regret(matching, preferences):
    return realistic_sided_regret(matching, preferences[::-1]) - realistic_sided_regret(matching, preferences)


def realistic_sided_regret(matching, preferences):
    optimal = gale_shapley(preferences)
    abs_reg = [regret(y, preferences[0][x]) for x, y in matching]
    opt_reg = [regret(y, preferences[0][x]) for x, y in optimal]
    return sum([i - j for i, j in zip(abs_reg, opt_reg)])


def regret(mate, pref):
    return pref.index(mate)
