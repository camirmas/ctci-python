def is_unique(string):
    """Determines if a string contains all unique characters."""
    values = {}

    for char in string:
        if values.get(char):
            return False
        values[char] = True
    
    return True
