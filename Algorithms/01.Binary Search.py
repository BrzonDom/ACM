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
            """"    If number at mid index is equal or grater than target
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
            """"    If number at mid index is equal or grater than target
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

        else:
            """"    If number at mid index is equal or grater than target
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

