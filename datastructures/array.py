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
            raise ValueError('Starting sequence must be a valid sequence type')
        for index in range(self.__logical_size):
            if not isinstance(starting_sequence[index], self.__data_type):
                raise TypeError('Items in starting sequence are not all same type')
        self.__items: NDArray = np.empty(self.__logical_size, dtype=self.__data_type)
        for index in range(self.__logical_size):
            self.__items[index] = deepcopy(starting_sequence[index])


        
        


    @overload
    def __getitem__(self, index: int) -> T:
        if not isinstance(index, int): 
            raise TypeError("Index must be an int or a slice")
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
        else: 
            raise TypeError("Index must be an int or a slice")
    
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, slice):
            start: int = index.start if not None else 0
            stop: int = index.stop if not None else -1
            step:int = index.step if not None else 1
            if start not in range(self.__logical_size) or stop not in range(self.__logical_size):
                raise IndexError("Index must be in array")
            sliced_items = self.__items[start:stop:step]
            return Array(starting_sequence=sliced_items.tolist(), data_type=self.__data_type) 
        elif isinstance(index, int):
            if index not in range(self.__logical_size):
                raise IndexError("Index must be in array")
            item = self.__items[index]
            return item.item() if isinstance(item, np.generic) else item
        else: 
            raise TypeError("Index must be an int or a slice")
        
    def __setitem__(self, index: int, item: T) -> None:
        if not isinstance(item, self.__data_type):
            raise TypeError("Item must be valid data type")
        if index not in range(self.__logical_size):
            raise IndexError("Index must be within array")
        else:
            self.__items[index] = item
               
    

    def append(self, data: T) -> None:
        app_index: int = self.__logical_size + 1
        if self.__logical_size == self.__physical_size:
            new_size = self.__physical_size * 2
            new_array: NDArray = np.empty(new_size, dtype=self.__data_type) 
            for i in range(len(self.__items)):
                new_array[i] = deepcopy(self.__items[i])
            self.__items = new_array
            self.__physical_size = new_size
        self.__items[app_index] = data
        self.__logical_size += 1 

    def append_front(self, data: T) -> None:
        if self.__logical_size == self.__physical_size:
            new_size = self.__physical_size * 2
            new_array: NDArray = np.empty(new_size, dtype=self.__data_type)
            new_array[0] = data 
            for i in range(len(self.__items)):
                new_array[i+1] = deepcopy(self.__items[i])
            self.__items = new_array
            self.__physical_size = new_size
        else:
            new_array: NDArray = np.empty(self.__physical_size, dtype=self.__data_type)
            new_array[0] = data
            for i in range(len(self.__items)):
                new_array[i+1] = deepcopy(self.__items[i])
                self.__items = new_array
        self.__logical_size += 1

    def pop(self) -> None:
        self.__logical_size -=1
        if self.__logical_size <= self.__physical_size//4:
            new_size = self.__physical_size//4
            new_array: NDArray = np.empty(new_size, dtype=self.__data_type) 
            for i in range(self.__logical_size):
                new_array[i] = deepcopy(self.__items[i])
            self.__items = new_array
            self.__physical_size = new_size
        else:
            new_array: NDArray = np.empty(self.__physical_size, dtype=self.__data_type) 
            for i in range(self.__logical_size):
                new_array[i] = deepcopy(self.__items[i])
            self.__items = new_array
    
    def pop_front(self) -> None:
        if len(self.__items) == 0:
            raise IndexError("Cannot remove object from empty array")
        else:
            self.__delitem__(index=0)

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
        reversed_list = list(self.__items[::-1])
        reversed_array: NDArray = np.array(reversed_list, dtype=self.__data_type)
        return(reversed_array)

    def __delitem__(self, index: int) -> None:
        for i in range(self.__logical_size):
            if i >= index and i+1 in range(len(self.__items)):
               self.__items[i] = self.__items[i+1]
        self.__logical_size -= 1
        if self.__logical_size <= self.__physical_size//4:
            new_size = self.__physical_size//4
            new_array: NDArray = np.empty(new_size, dtype=self.__data_type) 
            for i in range(self.__logical_size):
                new_array[i] = deepcopy(self.__items[i])
            self.__items = new_array
            self.__physical_size = new_size
        else:
            new_array: NDArray = np.empty(self.__physical_size, dtype=self.__data_type) 
            for i in range(self.__logical_size):
                new_array[i] = deepcopy(self.__items[i])
            self.__items = new_array
            

               

    def __contains__(self, item: Any) -> bool:
        return any(self.__items[i] == item for i in range(len(self.__items)))

    def clear(self) -> None:
        self.__items = np.array([], dtype=self.__data_type)
        self.__physical_size = 0
        self.__logical_size = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self.__items) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')