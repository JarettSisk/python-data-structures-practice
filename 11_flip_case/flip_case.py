def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # if string is lowercase and matches to_swap, than append uppercase
    newString = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.islower():
                newString += char.upper()
            elif char.isupper() == True:
                newString += char.lower()
        else:
            newString += char

    return newString
