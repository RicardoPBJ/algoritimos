from typing import List


def finder(nums, count):

    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        elif num in count:
            count[num] += 1
        else:
            count[num] = 1


def find_duplicate(nums: List[int]):

    if len(nums) <= 1 or not nums:
        return False

    count = {}

    finder(nums, count)

    for num, counter in count.items():
        if counter > 1:
            return num

    return False
