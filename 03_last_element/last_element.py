def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # if list is not empty, return last item, else return None
    return lst[len(lst) - 1] if len(lst) > 1 else None

