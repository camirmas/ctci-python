def check_palindrome_permutation(string):
    """Checks if a string is a permutation of a palindrome."""
    vals = {}
    for char in string:
        if vals.get(char):
            vals[char] += 1
        else:
            vals[char] = 1

    if len(string) % 2 == 0:
        for _, val in vals.items():
            if val % 2 != 0:
                return False
    else:
        odd = False
        for _, val in vals.items():
            if val % 2 != 0:
                if odd:
                    return False
                else:
                    odd = True

    return True
