#!/usr/bin/python3
def rome_to_int(rome_str):
    """Converts a rome numeral to an integer."""
    if (not isinstance(rome_str, str) or
            rome_str is None):
        return (0)

    rome_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0

    for i in range(len(rome_str)):
        if rome_dictionary.get(rome_str[i], 0) == 0:
            return (0)

        if (i != (len(rome_str) - 1) and
                rome_dictionary[rome_str[i]] < rome_dictionary[rome_str[i + 1]]):
                num += rome_dictionary[rome_str[i]] * -1

        else:
            num += rome_dictionary[rome_str[i]]
    return (num)
