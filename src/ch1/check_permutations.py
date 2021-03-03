def check_permutations(s1, s2):
    """Checks if two strings are permutations of one another."""
    s1_vals = {}
    for char in s1:
        if s1_vals.get(char):
            s1_vals[char] += 1
        else:
            s1_vals[char] = 1

    s2_vals = {}
    for char in s2:
        if s2_vals.get(char):
            s2_vals[char] += 1
        else:
            s2_vals[char] = 1
    
    for key in s1_vals:
        if s1_vals[key] != s2_vals[key]:
            return False
    
    return True
