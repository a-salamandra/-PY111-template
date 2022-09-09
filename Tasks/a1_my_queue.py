"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        print(elem)
        self.__queue.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if len(self.__queue) == 0:
            return None
        element = self.__queue.pop(0)
        return element


    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        print(ind)
        try:
            return self.__queue[ind]
        except IndexError:
            return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.__queue.clear()
        return None
