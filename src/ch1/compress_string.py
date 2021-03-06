def compress_string(string):
    compressed = ""

    idx = 0
    idx_2 = 0
    counter = 0
    current_char = None

    while idx < len(string):
        char = string[idx]

        current_char = char

        while idx_2 < len(string) and string[idx_2] == current_char:
            counter += 1
            idx_2 += 1

        compressed += "%s%s" % (char, counter)
        counter = 0
        idx = idx_2
        


    return compressed
