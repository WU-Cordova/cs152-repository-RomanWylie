from __future__ import annotations
import os
from typing import Iterator, Sequence

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int, data_type: type) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns
            self.data_type = data_type

        def __getitem__(self, column_index: int) -> T:
            if column_index not in range(self.num_columns):
                raise IndexError("Index must be within array")
            map_index = self.row_index*self.num_columns + column_index
            return self.array[map_index]
            
        
        def __setitem__(self, column_index: int, value: T) -> None:
            if column_index not in range(self.num_columns):
                raise IndexError("Index must be within array")
            if not isinstance(value, self.data_type):
                raise TypeError("Value must be of same type as array")
            map_index = self.row_index*self.num_columns + column_index
            self.array[map_index] = value
            
        
        def __iter__(self) -> Iterator[T]:
            for i in range(self.num_columns):
                yield self[i]
        
        def __reversed__(self) -> Iterator[T]:
            for i in range(self.num_columns-1, -1, -1):
                yield self[i]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError("Starting sequence must be a sequence of sequences")
        for i in range(len(starting_sequence)):
            if not isinstance(starting_sequence[i], Sequence):
                raise ValueError("Starting sequence must be a sequence of sequences")
        for i in range(len(starting_sequence)):
            for x in starting_sequence[i]:
                if not isinstance(x, data_type):
                    raise ValueError("Data must be of declared type")
        for i in range(len(starting_sequence)):
            if len(starting_sequence[0]) != len(starting_sequence[i]):
                raise ValueError("Rows must be of same length")
        self.__num_rows: int = len(starting_sequence)
        self.__num_columns: int = len(starting_sequence[0])
        self.__data_type: type = data_type
        row_major = []
        for i in range(len(starting_sequence)):
            for x in range(len(starting_sequence[i])):
                row_major.append(starting_sequence[i][x])
        self.__array: Array = Array(starting_sequence=row_major, data_type=data_type)
        
        
    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        empty_list: list[list] = [[data_type() for x in range(cols)] for i in range(rows)]
        return Array2D(starting_sequence=empty_list, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index not in range(self.__num_rows):
                raise IndexError("Index must be within array")
        return self.Row(row_index=row_index, array=self.__array, num_columns=self.__num_columns, data_type= self.__data_type)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for i in range(self.__num_rows):
            yield  self[i]
    
    def __reversed__(self):
        for i in range(self.__num_rows-1, -1, -1):
                yield self[i]
    
    def __len__(self): 
        return self.__num_rows
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')