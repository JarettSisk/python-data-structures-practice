def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count_dict = {}
    for char in phrase:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict