from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    print(elem, arr)

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < elem:
            low = mid + 1
        elif arr[mid] > elem:
            high = mid - 1
        else:
            return mid

    return None




