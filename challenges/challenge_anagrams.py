def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    left_half, right_half = merge_sort(string[:mid]), merge_sort(string[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    lft, r = 0, 0

    while lft < len(left) and r < len(right):
        if left[lft] <= right[r]:
            merged.append(left[lft])
            lft += 1
        else:
            merged.append(right[r])
            r += 1

    merged.extend(left[lft:])
    merged.extend(right[r:])

    return merged


def is_anagram(first_string: str, second_string: str):
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    first_ordened = ''.join(merge_sort(list(first_string.lower())))
    second_ordened = ''.join(merge_sort(list(second_string.lower())))

    return (first_ordened, second_ordened, first_ordened == second_ordened)
