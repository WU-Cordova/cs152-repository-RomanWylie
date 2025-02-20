# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
from copy import deepcopy, copy


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        self.__logical_size: int = len(starting_sequence)
        self.__physical_size: int = self.__logical_size
        self.__data_type: type = data_type
        if not isinstance(starting_sequence, Sequence):
            raise TypeError('Starting sequence must be a valid sequence type')
        for index in range(self.__logical_size):
            if not isinstance(starting_sequence[index], self.__data_type):
                raise TypeError('Items in starting sequence are not all same type')
        self.__items: NDArray = np.empty(self.__logical_size, dtype=self.__data_type)
        for index in range(self.__logical_size):
            self.__items[index] = deepcopy(starting_sequence[index])


        
        


    @overload
    def __getitem__(self, index: int) -> T:
        if index not in range(self.__logical_size):
            raise IndexError("Index must be in array")
        item = self.__items[index]
        return item.item() if isinstance(item, np.generic) else item
        
        
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]:
        if isinstance(index, slice):
            start = index.start if not None else 0
            stop = index.stop if not None else -1
            step = index.step if not None else 1
            if start in range(self.__logical_size) and start+step in range(self.__logical_size):
                raise IndexError("Index must be in array")
            sliced_items = self.__items[start:stop:step]
            return Array(starting_sequence=list(sliced_items), data_type=self.__data_type)
    
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, slice):
            start = index.start if not None else 0
            stop = index.stop if not None else -1
            step = index.step if not None else 1
            if start in range(self.__logical_size) and start+step in range(self.__logical_size):
                raise IndexError("Index must be in array")
            sliced_items = self.__items[start:stop:step]
            return Array(starting_sequence=list(sliced_items), data_type=self.__data_type) 
        elif isinstance(index, int):
            if index not in range(self.__logical_size):
                raise IndexError("Index must be in array")
            item = self.__items[index]
            return item.item() if isinstance(item, np.generic) else item
        
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item must be valid data type")
        if index not in range(self.__logical_size):
            raise IndexError("Index must be within array")
        else:
            self.__items[index] = item
               

    def append(self, data: T) -> None:
        raise NotImplementedError('Append not implemented.')

    def append_front(self, data: T) -> None:
        raise NotImplementedError('Append front not implemented.')

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        return(self.__logical_size)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        elif self.__logical_size != other.__logical_size:
            return False
        elif self.__items.all() == other.__items.all():
            return True
        else:
            return False
    
    def __iter__(self) -> Iterator[T]:
	    return iter(self.__items)
    
    def __reversed__(self) -> Iterator[T]:
        pass
    def __delitem__(self, index: int) -> None:
       raise NotImplementedError('Delete not implemented.')

    def __contains__(self, item: Any) -> bool:
        any(self.__items[i] is item for i in range(self.__logical_size))

    def clear(self) -> None:
        raise NotImplementedError('Clear not implemented.')

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')