"""
Binary Search Algorithm

https://www.geeksforgeeks.org/binary-search/

    Description:

        Binary Search is defined as a searching algorithm used in a sorted array by repeatedly
        dividing the search interval in half. The idea of binary search is to use the information
        that the array is sorted and reduce the time complexity to O(log N).

    Conditions:

        The data structure must be sorted.
        Access to any element of the data structure takes constant time.

"""

def binarySearch_Iter(arr, trg):

    print(f"Array:  {arr}")
    print(f"Target: {trg}")
    print()

    lft = 0
    rgt = len(arr) - 1

    while lft <= rgt:

        mid = lft + (rgt - lft) // 2

        if arr[mid] == trg:
            print()
            print(f"Index of target: {mid}")
            return mid

        elif arr[mid] < trg:
            lft = mid + 1
            print(f"\tTarget left  =>  {arr[lft:rgt+1]}")

        else:
            rgt = mid - 1
            print(f"\tTarget right =>  {arr[lft:rgt+1]}")


if __name__ == '__main__':
    arr = [2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 20, 25, 40]
    trg = 10

    print(f"Array:  {arr}")
    print(f"Target: {trg}")
    print()

    lft = 0
    rgt = len(arr) - 1

    while lft <= rgt:

        mid = lft + (rgt - lft) // 2

        if arr[mid] == trg:
            print()
            print(f"Index of target: {mid}")
            break

        elif arr[mid] < trg:
            lft = mid + 1
            print(f"\tTarget left  =>  {arr[lft:rgt+1]}")

        else:
            rgt = mid - 1
            print(f"\tTarget right =>  {arr[lft:rgt+1]}")