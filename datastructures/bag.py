from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.__bag: dict[T, int]={}
        if items:
            for item in items:
                self.add(item)

    def add(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] += 1
        elif item is None:
            raise TypeError("item cannot be None")
        else:
            self.__bag[item] = 1
    

    def remove(self, item: T) -> None:
        if item in self.__bag:
            self.__bag[item] -= 1
        else:
            raise ValueError("item not in bag")
            
    def count(self, item: T) -> int:
        if item in self.__bag:
            return self.__bag[item]
        else:
            return 0


    def __len__(self) -> int:
        total = 0
        for item in self.__bag:
            total += self.count(item)
        return total
    
    def distinct_items(self) -> Iterable[T]:
        return list(self.__bag)
            
            

    def __contains__(self, item) -> bool:
        if item in self.__bag:
            return True
        else:
            return False

    def clear(self) -> None:
        self.__bag: dict[T, int]={}