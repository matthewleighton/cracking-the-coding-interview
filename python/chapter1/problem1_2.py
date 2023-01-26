def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    
    string1_sorted = ''.join(sorted(string1))
    string2_sorted = ''.join(sorted(string2))

    if string1_sorted != string2_sorted:
        return False
    
    return True