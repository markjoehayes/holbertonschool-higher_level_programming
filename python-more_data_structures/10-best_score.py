#!/usr/bin/python3
def best_score(a_dictionary):
    scores = list(a_dictionary.values())
    i = 0
    for score in scores:
            high_score = score[i]
            i += 1
    return high_score
