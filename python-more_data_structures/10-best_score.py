#!/usr/bin/python3
def best_score(a_dictionary):
    scores = []
    i = 0
    for key, value in a_dictionary.items():
        scores.append(a_dictioanry(key))
    for score in scores:
        if score[i] > score[i + 1]:
            high_score = score[i]
            i += 1
    return high_score
        
