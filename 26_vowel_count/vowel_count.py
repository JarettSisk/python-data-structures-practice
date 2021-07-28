def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    isVowel = "aeiou"
    
    count_dict = {}
    for char in phrase.lower():
        if char in count_dict and char in isVowel:
            count_dict[char] += 1
        elif char in isVowel:
            count_dict[char] = 1

    return count_dict