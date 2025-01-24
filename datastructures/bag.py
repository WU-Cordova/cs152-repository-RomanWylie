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
        raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> Iterable[T]:
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        raise NotImplementedError("clear method not implemented")