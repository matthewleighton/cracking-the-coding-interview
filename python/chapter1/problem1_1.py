def has_unique_characters(string):
    original_length = len(string)
    test_length = len(set(string))

    if original_length == test_length:
        return True
    else:
        return False