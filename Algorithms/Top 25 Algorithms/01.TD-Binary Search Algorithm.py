"""
Binary Search Algorithm – Iterative and Recursive Implementation

https://www.techiedelight.com/binary-search/

    Given a sorted array of n integers and a target value,
    determine if the target exists in the array in logarithmic time
    using the binary search algorithm.
    If target exists in the array, print the index of it.


    The idea is to use binary search which is a Divide and Conquer algorithm.
    Like all divide-and-conquer algorithms, binary search first divides
    a large array into two smaller subarrays and then recursively (or iteratively)
    operate the subarrays. But instead of working on both subarrays,
    it discards one subarray and continues on the second subarray.
    This decision of discarding one subarray is made in just one comparison.

    So binary search reduces the search space to half at each step.
    By search space, we mean a subarray of the given array where
    the target value is located (if present in the array).
    Initially, the search space is the entire array,
    and binary search redefines the search space at every step
    of the algorithm by using the property of the array that it is sorted.


    Let’s track the search space by using two indexes – start and end. Initially, start = 0 and end = n-1
    (as initially, the whole array is our search space).
    At each step, find the mid-value in the search space and compares it
    with the target. There are three possible cases:

        If target = nums[mid], return mid.

        If target < nums[mid], discard all elements in the right search space,
                including the middle element, i.e., nums[mid…high]. Now our new high would be mid-1.

        If target > nums[mid], discard all elements in the left search space,
                including the middle element, i.e., nums[low…mid]. Now our new low would be mid+1.

    Repeat the process until the target is found, or our search space is exhausted.

"""


# Function to determine if a `target` exists in the sorted list `nums`
# or not using a binary search algorithm
def binarySearch_Iter(nums, target):
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)

    # loop till the search space is exhausted
    while left <= right:

        # find the mid-value in the search space and
        # compares it with the target

        mid = (left + right) // 2

        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2

        # target is found
        if target == nums[mid]:
            return mid

        # discard all elements in the right search space,
        # including the middle element
        elif target < nums[mid]:
            right = mid - 1

        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1

    # `target` doesn't exist in the list
    return -1


# Recursive implementation of the binary search algorithm to return
# the position of `target` in subarray nums[left…right]
def binarySearch_Recu(nums, left, right, target):
    # Base condition (search space is exhausted)
    if left > right:
        return -1

    # find the mid-value in the search space and
    # compares it with the target

    mid = (left + right) // 2

    # overflow can happen. Use below
    # mid = left + (right - left) / 2

    # Base condition (a target is found)
    if target == nums[mid]:
        return mid

    # discard all elements in the right search space,
    # including the middle element
    elif target < nums[mid]:
        return binarySearch_Recu(nums, left, mid - 1, target)

    # discard all elements in the left search space,
    # including the middle element
    else:
        return binarySearch_Recu(nums, mid + 1, right, target)


if __name__ == '__main__':

    print("01.TD-Binary Search Algorithm.py\n")

    nums = [2, 5, 6, 8, 9, 10]
    target = 5

    print(f"Array:  {nums}")
    print(f"Target: {target}")
    print()

    print("Iterative Implementation:\n")

    index = binarySearch_Iter(nums, target)

    if index != -1:
        print('\tElement found at index', index)
    else:
        print('\tElement found not in the list')

    print("\n")
    print("Recursive Implementation:\n")

    (left, right) = (0, len(nums) - 1)
    index = binarySearch_Recu(nums, left, right, target)

    if index != -1:
        print('\tElement found at index', index)
    else:
        print('\tElement found not in the list')