#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) <= 0:
        return None
    value1 = list(a_dictionary.values())[0]
    value2 = list(a_dictionary.keys())[0]
    for x, y in a_dictionary.items():
        if y > value1:
            value1 = y
            value2 = x
    return (value2)
