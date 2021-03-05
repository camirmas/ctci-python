def one_away(s1, s2):
    """
    Returns True if the two strings are <= 1 edit apart from each other.
    """
    if abs(len(s1)-len(s2)) > 1:
        return False

    vals_1 = {}

    for char in s1:
        if vals_1.get(char):
            vals_1[char] += 1
        else:
            vals_1[char] = 1

    vals_2 = {}

    for char in s2:
        if vals_2.get(char):
            vals_2[char] += 1
        else:
            vals_2[char] = 1

    changes = 0

    for key, val_1 in vals_1.items():
        if changes > 1:
            return False
        if not vals_2.get(key):
            changes += 1
        else:
            changes += abs(val_1-vals_2[key])

    return True
