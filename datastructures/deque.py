import os
from datastructures.iqueue import IQueue
from datastructures.linkedlist import LinkedList
from typing import TypeVar

T = TypeVar('T')

class Deque[T](IQueue[T]):
    """
    A double-ended queue (deque) implementation.
    """

    def __init__(self, data_type: type = object) -> None:
        """
        Initializes the deque with a specified data type.

        Args:
            - data_type (type): The type of data the deque will hold.
        """
        self._deque=LinkedList(data_type=data_type)

    def enqueue(self, item: T) -> None:
        """
        Adds an item to the back of the deque.

        Args:
            - item (T): The item to add to the back of the deque.

        Raises:
            - TypeError: If the item is not of the correct type.
        """
        self._deque.append(item)
    def dequeue(self) -> T:
        """
        Removes and returns the item from the front of the deque.

        Returns:
            - T: The item removed from the front of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        return self._deque.pop_front()
    def enqueue_front(self, item: T) -> None:
        """
        Adds an item to the front of the deque.

        Args:
            - item (T): The item to add to the front of the deque.

        Raises:
            - TypeError: If the item is not of the correct type.
        """
        self._deque.prepend(item)
    def dequeue_back(self) -> T:
        """
        Removes and returns the item from the back of the deque.

        Returns:
            - T: The item removed from the back of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        return self._deque.pop()
    def front(self) -> T:
        """
        Returns the front item of the deque without removing it.

        Returns:
            - T: The front item of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        return self._deque.front
    def back(self) -> T:
        """
        Returns the back item of the deque without removing it.

        Returns:
            - T: The back item of the deque.

        Raises:
            - IndexError: If the deque is empty.
        """
        return self._deque.back
    def empty(self) -> bool:
        """
        Checks if the deque is empty.

        Returns:
            - bool: True if the deque is empty, False otherwise.
        """
        return self._deque.empty
    def __len__(self) -> int:
        """
        Returns the number of items in the deque.

        Returns:
            - int: The number of items in the deque.
        """
        return self._deque.__len__()    
    def __contains__(self, item: T) -> bool:
        """
        Checks if an item exists in the deque.

        Args:
            - item (T): The item to check for existence.

        Returns:
            - bool: True if the item exists in the deque, False otherwise.
        """
        return self._deque.__contains__(item)    
    def __eq__(self, other) -> bool:
        """
        Compares two deques for equality.

        Args:
            - other (Deque): The deque to compare with.

        Returns:
            - bool: True if the deques are equal, False otherwise.
        """
        if isinstance(other, Deque):
            return self._deque.__eq__(other=other._deque) 
        else:
            return False   
    def clear(self):
        """
        Clears all items from the deque.
        """
        self._deque.clear()
    def __str__(self) -> str:
        """
        Returns a string representation of the deque.

        Returns:
            - str: A string representation of the deque.
        """
        return self._deque.__str__()    
    def __repr__(self) -> str:
        """
        Returns a detailed string representation of the deque.

        Returns:
            - str: A detailed string representation of the deque.
        """
        return self._deque.__repr__()

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
