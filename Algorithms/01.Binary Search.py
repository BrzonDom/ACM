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

def binarySearch_Iter(arr, trg):

    print(f"\tArray:  {arr}")
    print(f"\tTarget: {trg}")
    print()

    lft = 0
    rgt = len(arr) - 1

    while lft <= rgt:
        """     Base case check     """

        mid = lft + (rgt - lft) // 2

        if arr[mid] == trg:
            """     If number at mid index is target  
                        target index found, end iteration   """

            print()
            print(f"\tIndex of target: {mid}")

            return mid

        elif arr[mid] < trg:
            """"    If number at mid index is less than target
                        shift left index to mid + 1, continue iteration     """

            lft = mid + 1
            print(f"\t\tTarget left  =>  {arr[lft:rgt+1]}")

        else:
            """"    If number at mid index is grater than target
                        shift right index to mid - 1, continue iteration     """

            rgt = mid - 1
            print(f"\t\tTarget right =>  {arr[lft:rgt+1]}")

    """     Edge case return    """

    print("\tTarget not present in the array")
    return -1


def binarySearch_Recu(arr, trg, lft, rgt):

    if rgt >= lft:
        """     Base case check     """

        mid = lft + (rgt - lft) // 2

        if arr[mid] == trg:
            """     If number at mid index is target  
                        target index found, end recursion   """

            print()
            print(f"\tIndex of target: {mid}")

            return mid

        elif arr[mid] > trg:
            """"    If number at mid index is less than target
                        shift left index to mid + 1, continue recursion     """

            return binarySearch_Recu(arr, trg, lft, mid-1)

        else:
            """"    If number at mid index is grater than target
                        shift right index to mid - 1, continue recursion    """

            return binarySearch_Recu(arr, trg, mid+1, rgt)

    else:
        """     Edge case return    """

        print("\tTarget not present in the array")
        return -1


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 20, 25, 40]
    trg = 10

    print("Driver solution:\n")

    print(f"\tArray:  {arr}")
    print(f"\tTarget: {trg}")
    print()

    lft = 0
    rgt = len(arr) - 1

    while lft <= rgt:

        mid = lft + (rgt - lft) // 2

        if arr[mid] == trg:
            """     If number at mid index is target  
                        target index found, end iteration   """

            print()
            print(f"\tIndex of target: {mid}")
            break

        elif arr[mid] < trg:
            """"    If number at mid index is less than target
                        shift left index to mid + 1, continue iteration     """

            lft = mid + 1
            print(f"\t\tTarget left  =>  {arr[lft:rgt+1]}")

        elif arr[mid] > trg:
            """"    If number at mid index is grater than target
                        shift right index to mid - 1, continue iteration     """

            rgt = mid - 1
            print(f"\t\tTarget right =>  {arr[lft:rgt+1]}")

    print("\n")

    print("Iterative function solution:\n")

    trgInd = binarySearch_Iter(arr, trg)

    if trgInd == -1:
        print("\t\tTarget not present in the array")
    else:
        print(f"\t\tIndex of target: {trgInd}")

    print("\n")

    print("Recursive function solution:\n")

    print(f"\tArray:  {arr}")
    print(f"\tTarget: {trg}")

    trgInd = binarySearch_Recu(arr, trg, 0, len(arr)-1)

    if trgInd == -1:
        print("\t\tTarget not present in the array")
    else:
        print(f"\t\tIndex of target: {trgInd}")

