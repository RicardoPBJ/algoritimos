def is_palindrome_iterative(word):
    low_index = 0
    high_index = len(word)

    if len(word) == 0:
        return False

    while low_index < high_index:
        if word[low_index] != word[high_index - 1]:
            return False
        low_index += 1
        high_index -= 1
    return True
