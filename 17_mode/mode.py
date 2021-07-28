def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1

    current_num = 0
    for key in num_dict:
        if num_dict[key] > current_num:
            current_num = key
    return current_num

