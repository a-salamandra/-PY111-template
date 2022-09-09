"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priority_queue = {i : [] for i in range(0,11)}  # для очереди можно использовать python dict

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        if not isinstance(priority, int):
            raise TypeError ("queue priorities should be integers")
        if priority < 0 or priority > 10:
            raise ValueError ("queue priorities should be from 0 to 10")

        self.priority_queue[priority].append(elem)


    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.priority_queue:
            return None

        for key, item in self.priority_queue.items():
            if item:
                return self.priority_queue[key].pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if not self.priority_queue:
            return None

        if priority not in self.priority_queue:
            raise ValueError ("incorrect priority value")
        elif 0 <= ind < len(self.priority_queue[priority]):
            return self.priority_queue[priority][ind]
        else:
            return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priority_queue.clear()
        self.__init__()
        return None