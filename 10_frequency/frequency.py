def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    # set initial count to be 0
    count = 0
    # If item matches search term, add 1 to count
    for item in lst:
        if item == search_term:
            count += 1

    return count



