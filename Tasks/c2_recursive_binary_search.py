from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    def search(elem, arr, left, right):
        if left > right:
            return None

        middle = (left + right) // 2

        if elem == arr[middle]:
            return middle
        elif elem < arr[middle]:
            return search(elem, arr, left, middle-1)
        else:
            return search(elem, arr, middle+1, right)

    left = 0
    right = len(arr) - 1
    return search(elem, arr, left, right)


